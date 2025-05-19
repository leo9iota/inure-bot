from typing import Dict, Optional, Any, Tuple
from enum import Enum, auto
from decimal import Decimal


class TradeType(Enum):
    """Types of trades."""
    BUY = auto()
    SELL = auto()


class TradeStatus(Enum):
    """Status of a trade."""
    PENDING = auto()
    EXECUTED = auto()
    CANCELLED = auto()
    FAILED = auto()


class TradingStrategy:
    """Base class for trading strategies."""

    def __init__(self, name: str, risk_level: int = 1) -> None:
        """Initialize the trading strategy.

        Args:
            name: The name of the strategy
            risk_level: Risk level from 1 (low) to 5 (high)
        """
        self.name: str = name
        self.risk_level: int = max(1, min(5, risk_level))  # Clamp between 1-5

    def generate_signal(self, market_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Generate a trading signal based on market data.

        Args:
            market_data: Market data to analyze

        Returns:
            A signal dictionary or None if no signal is generated
        """
        raise NotImplementedError("Subclasses must implement generate_signal method")


class Trade:
    """Represents a trade in the system."""

    def __init__(
        self,
        symbol: str,
        trade_type: TradeType,
        quantity: Decimal,
        price: Decimal,
        strategy_name: str
    ) -> None:
        """Initialize a trade.

        Args:
            symbol: Trading symbol (e.g., BTC/USD)
            trade_type: Type of trade (BUY or SELL)
            quantity: Amount to trade
            price: Price at which to execute the trade
            strategy_name: Name of the strategy that generated this trade
        """
        self.symbol: str = symbol
        self.trade_type: TradeType = trade_type
        self.quantity: Decimal = quantity
        self.price: Decimal = price
        self.strategy_name: str = strategy_name
        self.status: TradeStatus = TradeStatus.PENDING

    def execute(self) -> Tuple[bool, str]:
        """Execute the trade.

        Returns:
            A tuple of (success, message)
        """
        # Implementation will connect to exchange API
        self.status = TradeStatus.EXECUTED
        return (True, f"Executed {self.trade_type.name} trade for {self.quantity} {self.symbol} at {self.price}")

    def cancel(self) -> bool:
        """Cancel the trade if it's still pending.

        Returns:
            True if cancelled successfully, False otherwise
        """
        if self.status == TradeStatus.PENDING:
            self.status = TradeStatus.CANCELLED
            return True
        return False