from src.util.get_api_consumer import GetApiConsumer
from src.data.usescases.startships_information_colector import StarshipsInformationColector
from src.presenters.controllers.startships_Information_colector_controller import StarshipsInformationColetorController


def get_starships_information_composers():
    """Composer"""
    infra = GetApiConsumer()
    usecase = StarshipsInformationColector(infra)
    controller = StarshipsInformationColetorController(usecase)

    return controller
