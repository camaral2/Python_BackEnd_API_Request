from src.util.get_api_consumer import GetApiConsumer
from src.data.usescases.startships_list_colector import StarshipsListColector
from src.presenters.controllers.startships_list_colector_controller import (
    StarshipsListColetorController,
)


def get_starships_in_pagination_composers():
    """Composer"""
    infra = GetApiConsumer()
    usecase = StarshipsListColector(infra)
    controller = StarshipsListColetorController(usecase)

    return controller
