from vnpy.event import EventEngine
from vnpy.trader.engine import MainEngine
from vnpy.trader.ui import MainWindow, create_qapp
from vnpy_algotrading import AlgoTradingApp
from vnpy_chartwizard import ChartWizardApp
from vnpy_ctabacktester import CtaBacktesterApp
from vnpy_ctastrategy import CtaStrategyApp
from vnpy_datamanager import DataManagerApp
from vnpy_datarecorder import DataRecorderApp
from vnpy_excelrtd import ExcelRtdApp
from vnpy_optionmaster import OptionMasterApp
from vnpy_paperaccount import PaperAccountApp
from vnpy_portfoliomanager import PortfolioManagerApp
from vnpy_portfoliostrategy import PortfolioStrategyApp
from vnpy_riskmanager import RiskManagerApp
from vnpy_rpcservice import RpcServiceApp
from vnpy_scripttrader import ScriptTraderApp
from vnpy_spreadtrading import SpreadTradingApp
from vnpy_webtrader import WebTraderApp


# from vnpy_ctp import CtpGateway  # TODO X: macos fix, https://github.com/vnpy/vnpy_ctp


def main():
    """Start VeighNa Trader
    基于 Qt 实现的 GUI 交易工具

    """
    qapp = create_qapp()

    event_engine = EventEngine()
    main_engine = MainEngine(event_engine)

    # main_engine.add_gateway(CtpGateway)  # TODO X: macos fix, https://github.com/vnpy/vnpy_ctp
    main_engine.add_app(CtaStrategyApp)  # CTA策略引擎模块
    main_engine.add_app(CtaBacktesterApp)  # CTA策略回测模块

    #
    # ref: https://www.vnpy.com/docs/cn/community/app/spread_trading.html
    #
    main_engine.add_app(SpreadTradingApp)  # 价差交易模块，支持自定义价差，实时计算价差行情和持仓，支持价差算法交易以及自动价差策略两种模式
    main_engine.add_app(OptionMasterApp)  # 期权交易模块
    main_engine.add_app(PortfolioStrategyApp)  # 组合策略模块，面向同时交易多合约的量化策略（Alpha、期权套利等）
    main_engine.add_app(AlgoTradingApp)  # 算法交易模块，提供多种常用的智能交易算法：TWAP、Sniper、Iceberg、BestLimit等
    main_engine.add_app(ScriptTraderApp)  # 脚本策略模块
    main_engine.add_app(PaperAccountApp)  # 本地仿真模块，纯本地化实现的仿真模拟交易功

    #
    # ref: https://www.vnpy.com/docs/cn/community/app/chart_wizard.html
    #
    main_engine.add_app(ChartWizardApp)  # K线图表模块
    main_engine.add_app(PortfolioManagerApp)  # 交易组合管理模块
    main_engine.add_app(RpcServiceApp)  # RPC服务模块
    main_engine.add_app(DataManagerApp)  # 历史数据管理模块
    main_engine.add_app(DataRecorderApp)  # 行情记录模块
    main_engine.add_app(ExcelRtdApp)  # Excel RTD（Real Time Data）实时数据服务，基于pyxll模块实现在Excel中获取各类数据（行情、合约、持仓等）的实时推送更新
    main_engine.add_app(WebTraderApp)  # Web服务模块
    main_engine.add_app(RiskManagerApp)  # 风险管理模块

    #
    # QT GUI Window
    #
    main_window = MainWindow(main_engine, event_engine)
    main_window.showMaximized()

    qapp.exec()


if __name__ == "__main__":
    main()
