from abc import ABC, abstractmethod
from typing import Any

from app.domain.entities.auctionBE import AuctionBE
from app.domain.entities.bidBE import BidBE


class IAuctionRepository(ABC):
    @abstractmethod
    async def get(self, **filters: Any) -> AuctionBE | None:
        pass

    @abstractmethod
    async def add_bid(self, bid: BidBE) -> bool:
        pass