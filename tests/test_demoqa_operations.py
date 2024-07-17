import allure

from demoqa_tests.pages.registration_page import PracticeFormPage

registration_form = PracticeFormPage()
@allure.title('Successful fill form')
def test_open_page():
    registration_form.open()

def test_complete_demoqa():
    # WHEN
    registration_form.fill_first_name('Petr')
    registration_form.fill_last_name('Andreev')
    registration_form.fill_user_number('12345678998')
    registration_form.fill_user_email('for_example@gmail.com')
    registration_form.fill_gender()
    registration_form.fill_birthday('1999', 'May', '28')
    registration_form.fill_subjects('Computer Science')
    registration_form.fill_checkbox('Sports')
    registration_form.fill_checkbox('Music')
    registration_form.fill_foto('foto.png')
    registration_form.fill_address('Нижегородская обл, г Выкса')
    registration_form.fill_state('Haryana')
    registration_form.fill_city('Panipat')
    registration_form.submit()

def test_should_form_completion():
    # THEN
    registration_form.successful_authentication('Thanks for submitting the form')

    registration_form.should_registered_user_data(
        'Petr Andreev',
        'for_example@gmail.com',
        'Male',
        '1234567899',
        '28 May,1999',
        'Computer Science',
        'Sports, Music',
        'foto.png',
        'Нижегородская обл,'
        ' г Выкса',
        'Haryana Panipat'
    )
