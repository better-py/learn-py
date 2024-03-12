import datetime


def test_all():
    ts = "1710246453562"

    date = datetime.datetime.fromtimestamp(int(ts) / 1000)

    print(f"ts: {ts}, date: {date}")

    start_at = "2018-01-01 00:00:00"
    start_ts = int(datetime.datetime.strptime(start_at, "%Y-%m-%d %H:%M:%S").timestamp() * 1000)
    print(f"start at: {start_at}, ts:{start_ts}")

    print(f"ts length: {len(ts)}, {len(str(int(start_ts)))}")

    now_at = datetime.datetime.now()
    now_ts = int(now_at.timestamp() * 1000)

    print(f"now at : {now_at}, now_ts: {now_ts}, {len(str(int(now_ts)))}")
