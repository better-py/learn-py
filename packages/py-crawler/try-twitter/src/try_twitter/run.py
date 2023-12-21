import requests
import bs4
from loguru import logger
import datetime
import typer
import random

app = typer.Typer()


class WebTweet(object):
    """
    web post require http headers:
         headers={
            "content-type": "application/json",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
            "Authorization": "xxx",
            "Cookie": "xxx",
            "X-Csrf-Token": "xxx",
        }

    """

    API_CREATE_TWEET_URL = (
        "https://twitter.com/i/api/graphql/bDE2rBtZb3uyrczSZ_pI9g/CreateTweet"
    )
    API_DELETE_TWEET_URL = (
        "https://twitter.com/i/api/graphql/VaenaVgh5q5ih7kvyVjgtg/DeleteTweet"
    )

    def __init__(
        self,
        headers: dict = None,
        authorization: str = None,
        cookies: dict | str = None,
        csrf_token: str = None,
    ):
        self.headers = {
            "content-type": "application/json",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
            "Authorization": "",
            "Cookie": "",
            "X-Csrf-Token": "",
        }

        if headers and isinstance(headers, dict):
            for k, v in headers.items():
                self.headers[k] = v

        if authorization:
            self.headers["Authorization"] = authorization

        if cookies:
            self.headers["Cookie"] = cookies

        if csrf_token:
            self.headers["X-Csrf-Token"] = csrf_token

        logger.info(f"headers: {self.headers}")
        self.validate_headers()

        assert (
            self.headers["X-Csrf-Token"]
            and self.headers["Cookie"]
            and self.headers["Authorization"]
        )

    def validate_headers(self):
        if (
            not self.headers["X-Csrf-Token"]
            or not self.headers["Cookie"]
            or not self.headers["Authorization"]
        ):
            logger.error(
                f"❌ headers: {self.headers}, required headers: X-Csrf-Token, Cookie, Authorization"
            )
            return False

        return True

    def create_tweet(self, tweet: str = None):
        tweet = (
            tweet
            or f"post by twitter bot, ❤️ lucky number: {random.randint(1, 100)}, {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        )

        data = {
            "variables": {
                "tweet_text": f"{tweet}",
                "dark_request": False,
                "media": {"media_entities": [], "possibly_sensitive": False},
                "semantic_annotation_ids": [],
            },
            "features": {
                "c9s_tweet_anatomy_moderator_badge_enabled": True,
                "tweetypie_unmention_optimization_enabled": True,
                "responsive_web_edit_tweet_api_enabled": True,
                "graphql_is_translatable_rweb_tweet_is_translatable_enabled": True,
                "view_counts_everywhere_api_enabled": True,
                "longform_notetweets_consumption_enabled": True,
                "responsive_web_twitter_article_tweet_consumption_enabled": False,
                "tweet_awards_web_tipping_enabled": False,
                "longform_notetweets_rich_text_read_enabled": True,
                "longform_notetweets_inline_media_enabled": True,
                "rweb_video_timestamps_enabled": True,
                "responsive_web_graphql_exclude_directive_enabled": True,
                "verified_phone_label_enabled": False,
                "freedom_of_speech_not_reach_fetch_enabled": True,
                "standardized_nudges_misinfo": True,
                "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": True,
                "responsive_web_media_download_video_enabled": False,
                "responsive_web_graphql_skip_user_profile_image_extensions_enabled": False,
                "responsive_web_graphql_timeline_navigation_enabled": True,
                "responsive_web_enhance_cards_enabled": False,
            },
            "queryId": "bDE2rBtZb3uyrczSZ_pI9g",
        }

        r = requests.post(
            self.API_CREATE_TWEET_URL,
            headers=self.headers,
            json=data,
        )
        logger.info(f"📒create tweet, content: {tweet}")
        if r.status_code != 200:
            logger.error(f"❌create tweet error, {r.status_code}, {r.text}")
            return None
        logger.info(f"✅create tweet success, {r.status_code}")
        return r.json()

    def delete_tweet(self, tweet_id: str = None):
        data = {}
        return requests.post(
            self.API_DELETE_TWEET_URL,
            headers=self.headers,
            json=data,
        )


@app.command("create")
def create_tweet(
    authorization: str = None,
    cookies: str = None,
    csrf: str = None,
):
    import os

    authorization = authorization or os.getenv("TWITTER_AUTHORIZATION", "")
    cookies = cookies or os.getenv("TWITTER_COOKIES", "")
    csrf = csrf or os.getenv("TWITTER_CSRF_TOKEN", "")

    logger.info(
        f"🚀run, authorization: {authorization}, cookies: {cookies}, csrf_token: {csrf}"
    )

    t = WebTweet(authorization=authorization, cookies=cookies, csrf_token=csrf)
    t.create_tweet()


@app.command("del")
def delete_tweet(
    authorization: str = None, cookies: str = None, csrf_token: str = None
):
    logger.info(
        f"🚀run, authorization: {authorization}, cookies: {cookies}, csrf_token: {csrf_token}"
    )
    t = WebTweet(authorization=authorization, cookies=cookies, csrf_token=csrf_token)
    t.delete_tweet()


if __name__ == "__main__":
    # t = WebTweet()
    # t.create_tweet()

    app()
