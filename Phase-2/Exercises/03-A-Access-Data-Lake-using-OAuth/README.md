# Access Azure Data Lake Storage Gen2 using OAuth 2.0 with an Azure service principal
- Can securely access data in an Azure Data Lake Storage Gen2 (ADLS Gen2) account using OAuth 2.0 with an Azure Active Directory (Azure AD) application service principal for authentication

## Register an Azure Active Directory application
```
az account set --subscription 34ea504b-f779-4be0-892d-f968f164113d
az ad sp create-for-rbac -n "spDataBricksDataLake2" --skip-assignment
```

## What is secret scope:
- Collection of secrets identified by a name
- A workspace is limited to a maximum of 100 secret scopes
- A Databricks-backed secret scope is stored in (backed by) an encrypted database owned and managed by Databricks
- Can ben readable by all users in the workspace
### Scope permissions
- In account with Premium plan, can assign granular permissions at any time after you create the scope

## Setup Databricks CLI
- Open Azure Cloud Shell
- Run below commands:
```
virtualenv -p /usr/bin/python2.7 databrickscli
source databrickscli/bin/activate
pip install databricks-cli
```
- Collect databricks hostname. Below is the sample host name
```
https://adb-427238233502831.11.azuredatabricks.net
```
- Generate token
  - Open Databricks workspace
  - Click Username on top right and chose User Settings
  - Generate token

- Run below command
```
databricks configure --token
```
- Verify if you are able to view the databricks clusters
```
databricks clusters list
databricks fs ls
```

## Databricks CLI Sample commands for scopes
```
databricks secrets create-scope --scope <scope-name>
databricks secrets list-scopes
databricks secrets delete-scope --scope <scope-name>
```

## Add the client secret to a secret scope
```
databricks secrets create-scope --scope scope_app_secret
databricks secrets put --scope scope_app_secret --key app_secret_key
```

## Create a container in Data Lake storage account

## Assign roles
- Open container\Access Control (IAM)
- Assign role - "Storage Blob Data" to app "spDataBricksDataLake2"

## Mount ADLS Gen2 storage
- Run the following in your notebook to authenticate and create a mount point
```
configs = {"fs.azure.account.auth.type": "OAuth",
          "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
          "fs.azure.account.oauth2.client.id": "<application-id>",
          "fs.azure.account.oauth2.client.secret": dbutils.secrets.get(scope="<scope-name>",key="<service-credential-key-name>"),
          "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/<directory-id>/oauth2/token"}
```

```
dbutils.fs.mount(
  source = f"abfss://{container_name}@{storage_account_name}.dfs.core.windows.net/",
  mount_point = f"/mnt/{mount_name}",
  extra_configs = configs)
```

- Access files in your ADLS Gen2 filesystem as if they were files in DBFS
```
df = spark.read.csv(f"/mnt/{mount_name}/data/2015-summary.csv")
display(df)
```

- To unmount a mount point, use the following command
```
dbutils.fs.unmount(f"/mnt/{mount_name}")
```
