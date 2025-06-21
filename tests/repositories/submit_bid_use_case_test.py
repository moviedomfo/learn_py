import uuid

import pytest

from app.adapters.repositories.auction_repository.in_memory_repository import (
    InMemoryAuctionRepository,
)
from app.ports.repositories.auction_repository import AuctionRepository
from tests.utils import create_bid
from app.use_cases.exceptions import AuctionNotFoundError
from app.use_cases.submit_bid_use_case import SubmitBidUseCase


@pytest.fixture
def auctions_repository() -> AuctionRepository:
    return InMemoryAuctionRepository()


@pytest.fixture
def submit_bid_use_case(auctions_repository: AuctionRepository) -> SubmitBidUseCase:
    return SubmitBidUseCase(auctions_repository)


async def test_auction_not_found(submit_bid_use_case: SubmitBidUseCase):
    bid = create_bid(auction_id=uuid.uuid4())
    with pytest.raises(AuctionNotFoundError):
        await submit_bid_use_case(bid)