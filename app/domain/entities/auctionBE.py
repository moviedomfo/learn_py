from dataclasses import dataclass, field
from datetime import date
from uuid import UUID, uuid4

from domain.entities.bidBE import BidBE
from domain.entities.itemBE import ItemBE
from domain.value_objects.priceVO import Price


@dataclass
class AuctionBE:
    item: ItemBE
    seller_id: UUID
    start_date: date
    end_date: date
    start_price: Price
    bids: list[BidBE] = field(default_factory=list)
    id: UUID = field(default_factory=uuid4)

    @property
    def is_active(self) -> bool:
        return self.start_date <= date.today() <= self.end_date

    @property
    def minimal_bid_price(self) -> Price:
        return max(
            [bid.price for bid in self.bids] + [self.start_price], key=lambda x: x.value
        )