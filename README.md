
## 1 Install Node.js, npm and CDK

Use EC2 AMI:`Deep Learning AMI (Ubuntu 18.04) `

Download node.js

```shell
wget https://nodejs.org/dist/v16.13.1/node-v16.13.1-linux-x64.tar.xz
```



Copy node.js to` /usr/local/lib/node.js`

```shell
sudo mkdir -p /usr/local/lib/nodejs
tar xvf node-v16.13.1-linux-x64.tar.xz 
sudo mv node-v16.13.1-linux-x64/ /usr/local/lib/nodejs/node-v16.13.1-linux-x64/
```



Edit `/etc/profile` to add following line at the end of txt

```shell
export PATH=/usr/local/lib/nodejs/node-v16.13.1-linux-x64/bin:$PATH
```


Edit `/etc/sudoers` to add following content to the `secure_path` variable

```shell
/usr/local/lib/nodejs/node-v16.13.1-linux-x64/bin:
```



Logout and then login again, and then install CDK



```shell
source /etc/profile

sudo npm install -g aws-cdk

cdk --version
```

## 2 Run CDK

Download this artifact

```shell
git clone https://github.com/mlzoo/CDK-API-Gateway-Lambda-Python.git


cd CDK-API-Gateway-Lambda-Python
```

In the root path of this artifact, install needed python modules:

```shell
conda activate python3
pip3 install -r requirements.txt
```

And bootstrap the CDK

```shell
cdk bootstrap
```

And then run:

```shell
cdk deploy
```

The output will be

Outputs:
ApigatewayLambdaStack.WidgetsmlapiEndpoint79472A20 = https://xxx.execute-api.us-east-1.amazonaws.com/prod/
