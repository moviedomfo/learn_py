from app.domain.entities.personDTO import dto_to_entity

from app.domain.entities.auctionBE import AuctionBE
from app.domain.entities.bidBE import BidBE
from app.ports.repos.IAuctionRepository import IAuctionRepository
from typing import Any
from motor.motor_asyncio import AsyncIOMotorClient

class MongoRepository(IAuctionRepository):
    def __init__(self, client: AsyncIOMotorClient):
        self.collection = client.auctions.auction

    async def get(self, **filters: Any) -> AuctionBE | None:
        auction_data = await self.db.auctions.find_one(filters)
        if auction_data:
            return dto_to_entity(auction_data)
        return None

    async def add_bid(self, bid: BidBE) -> bool:
        result = await self.db.auctions.update_one(
            {"_id": bid.auction_id},
            {"$push": {"bids": bid.model_dump()}}
        )
        return result.modified_count > 0