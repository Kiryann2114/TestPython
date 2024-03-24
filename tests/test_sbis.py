from pages.contacts_page import ContactsPage
from pages.download_page import DownloadPage


def test_1(browser):
    contact_page = ContactsPage(browser)
    contact_page.open_sbis_go_contacts()
    contact_page.click_tensor_go_tensor()
    contact_page.check_strength_is_in_people()
    contact_page.click_details_check_about()
    contact_page.check_working_image()


def test_2(browser):
    contact_page = ContactsPage(browser)
    contact_page.open_sbis_go_contacts()
    contact_page.check_my_regoin()
    contact_page.chenge_region()
    contact_page.check_41_regoin()


def test_3(browser):
    download_page = DownloadPage(browser)
    download_page.open_sbis_go_download()
    download_page.download_sbis_plugin()
    download_page.check_file_size()
