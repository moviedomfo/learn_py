from typing import Any

from app.domain.entities.auctionBE import AuctionBE
from app.domain.entities.bidBE import BidBE
from app.ports.repos import IAuctionRepository


class InMemoryAuctionRepository(IAuctionRepository):
    auctions: list[AuctionBE] = []

    async def get(self, **filters: Any) -> AuctionBE | None:
        for auction in self.auctions:
            if (f := filters.get("id")) and f == auction.id:
                return auction
        return None

    async def add_bid(self, bid: BidBE) -> bool:
        for auction in self.auctions:
            if auction.id == bid.auction_id:
                auction.bids.append(bid)
                return True
        return False