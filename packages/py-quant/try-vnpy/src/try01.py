from vnpy.event import EventEngine
from vnpy.trader.engine import MainEngine
from vnpy.trader.ui import MainWindow, create_qapp
from vnpy_ctabacktester import CtaBacktesterApp
from vnpy_ctastrategy import CtaStrategyApp
from vnpy_spreadtrading import SpreadTradingApp


# from vnpy_ctp import CtpGateway  # TODO X: macos fix, https://github.com/vnpy/vnpy_ctp


def main():
    """Start VeighNa Trader"""
    qapp = create_qapp()

    event_engine = EventEngine()
    main_engine = MainEngine(event_engine)

    # main_engine.add_gateway(CtpGateway)  # TODO X: macos fix, https://github.com/vnpy/vnpy_ctp
    main_engine.add_app(CtaStrategyApp)
    main_engine.add_app(SpreadTradingApp)
    main_engine.add_app(CtaBacktesterApp)

    main_window = MainWindow(main_engine, event_engine)
    main_window.showMaximized()

    qapp.exec()


if __name__ == "__main__":
    main()
