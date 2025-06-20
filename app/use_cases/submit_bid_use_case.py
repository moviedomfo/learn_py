from domain.enitites.bid import Bid
from ports.repositories.auction_repository import AuctionRepository


class SubmitBidUseCase:
    def __init__(self, auction_repository: AuctionRepository):
        self._auction_repository = auction_repository

    async def __call__(self, bid: Bid) -> None: ...