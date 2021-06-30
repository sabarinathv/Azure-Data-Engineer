# Access Azure Blob Storage from Azure Databricks using Azure Key Vault
 - Refer: https://docs.microsoft.com/en-us/azure/databricks/scenarios/store-secrets-azure-key-vault

## Create a storage account and blob container
 - Copy Access Key - key1 and note in text notepad
 ```
XMM0I5ErfVBkKX0mlmlt8dC2GdFOFxf+cEGIjhcAc6NbVEHjjWi9QvN9Pstf1wz7OB098aX1AXIubLX0zUKq+A==
 ```

## Create an Azure Key Vault and add a secret
 - keyvault name - kvatindb21
 - Create a secret and in value put access key we copied in previous step
 - Note secret name in text notepad
 ```
 secretatindb21
 ```
 - Navigate to Properties tab of Key Vault and note DNS Name and Resource ID
 ```
 https://kvatindb21.vault.azure.net/
 /subscriptions/528dc260-e366-4d50-bd60-9b1e5ea1bcac/resourceGroups/rgJuly21/providers/Microsoft.KeyVault/vaults/kvatindb21
 ```

## Create an Azure Databricks workspace and add a secret scope
- Create Databricks workspace
- Once your Azure Databricks workspace is open in a separate window, append #secrets/createScope to the URL
- The URL should have the following format:
  - https://<\location>.azuredatabricks.net/?o=<\orgID>#secrets/createScope
  ```
  https://adb-427238233502831.11.azuredatabricks.net/?o=427238233502831#secrets/createScope
  ```
- Enter a scope name, DNS name and Resource ID you saved earlier
```
scopeatindb21
https://kvatindb21.vault.azure.net/
/subscriptions/528dc260-e366-4d50-bd60-9b1e5ea1bcac/resourceGroups/rgJuly21/providers/Microsoft.KeyVault/vaults/kvatindb21
```
- Save the scope name in notepad

## Access your blob container from Azure Databricks
- Create a new cluster and a new Python notebook
- Paste below in notebook
```
storage_account_name = "dbsaatin"
container_name = "dbcontainer1"
mount_name = "mntdbcontainer1"
# If using access key:
conf_key = f"fs.azure.account.key.{storage_account_name}.blob.core.windows.net"
# If using SAS of the container
conf_key = f"fs.azure.sas.{container_name}.{storage_account_name}.blob.core.windows.net"
scope_name = "scopeatindb21"
key_name = "secretatindb21"
```

```
dbutils.fs.mount(
source = f"wasbs://{container_name}@{storage_account_name}.blob.core.windows.net",
mount_point = f"/mnt/{mount_name}",
extra_configs = {f"{conf_key}":dbutils.secrets.get(scope = f"{scope_name}", key = f"{key_name}")})
```

```
file_name = ""
df = spark.read.text(f"/mnt/{mount_name}/{file_name}")
display(df)
```

```
dbutils.fs.unmount("/mnt/{mount_name}")
```
