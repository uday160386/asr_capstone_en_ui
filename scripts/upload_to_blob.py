from azure.storage.blob import BlobClient, ContentSettings

connection_string = "DefaultEndpointsProtocol=https;AccountName=asrblobstorage;AccountKey=VmCgMfZS1QJa7WuU6PwN4nhnIrnYfskgFG9mNqKcG7yZAwtPwrgX29u3fIriJVPDTJE0GMmJRC8D+ASttEjzbg==;EndpointSuffix=core.windows.net"
def upload_wav_file_content_to_Blob(blobname, wav_content):
    blob = BlobClient.from_connection_string(conn_str=connection_string, container_name="asrcontainer", blob_name=blobname)
    blob.upload_blob(wav_content)




