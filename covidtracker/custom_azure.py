from storages.backends.azure_storage import AzureStorage

class AzureStaticStorage(AzureStorage):
    account_name = 'covidtrackerindia' # Must be replaced by your storage_account_name
    account_key = 'I/uTwOPYXSyNRQY8EeYoa3d1iHYIUz9L1tDf8J2asWrjE8eqQs22dWCLFTygtlhms27Cgm2nMbm+HaI6ru6sBQ==' # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None