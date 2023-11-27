from configparser import ConfigParser


class ConfigReader:
    config = ConfigParser()
    config.read("config/config.properties")

    @staticmethod
    def get_base_url():
        return ConfigReader.config.get('BASICINFO', 'URL')

    @staticmethod
    def get_browser():
        return ConfigReader.config.get('BASICINFO', 'BROWSER')

    @staticmethod
    def get_account_page_title():
        return ConfigReader.config.get('ExpectedTitles', 'account_page')

    @staticmethod
    def get_login_page_title():
        return ConfigReader.config.get('ExpectedTitles', 'login_page')

    @staticmethod
    def get_invalid_credentials_warning():
        return ConfigReader.config.get('Messages', 'invalid_credentials_warning')

    @staticmethod
    def get_account_created_success_message():
        return ConfigReader.config.get('Messages', 'account_created_success')

    @staticmethod
    def get_duplicate_email_warning():
        return ConfigReader.config.get('Messages', 'duplicate_email_warning')

    @staticmethod
    def get_warning_messages():
        return [
            ConfigReader.config.get('EmptyFieldsWarningMessages', 'privacy_policy'),
            ConfigReader.config.get('EmptyFieldsWarningMessages', 'first_name_length'),
            ConfigReader.config.get('EmptyFieldsWarningMessages', 'last_name_length'),
            ConfigReader.config.get('EmptyFieldsWarningMessages', 'invalid_email'),
            ConfigReader.config.get('EmptyFieldsWarningMessages', 'telephone_length'),
            ConfigReader.config.get('EmptyFieldsWarningMessages', 'password_length'),
        ]

    @staticmethod
    def get_no_search_results_message():
        return ConfigReader.config.get('Messages', 'no_search_results')

    @staticmethod
    def get_products():
        return {
            'valid_product': ConfigReader.config.get('Products', 'valid_product'),
            'invalid_product': ConfigReader.config.get('Products', 'invalid_product')
        }

