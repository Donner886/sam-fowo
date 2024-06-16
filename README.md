### SAM CLI to execute CI/CD instruction
1, sam  build
2, sam deploy --guided or 
3, sam deploy --guilded --parameter-overrides Env=prod
variable ENV will specify the environment where the application is deployed. 

## Lambda function
1, If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.
2, version will help to identify the code status    


### when the lambda function is ready to interaction with dynamodb, 
the auth of CRUD on database should be granted. 
1, dynamodb, create_table, AttributionDefinitions should only contain the attributes in keySchema
2, 请注意， 可能会有不同的table记录family tree的不同财务状况， 但是不同 familyid会在表名称的最后体现。
3， 当RPA获取到estatement数据之后， 首先在dev环境校验，然后上传到prod

### S3 event notification.
1, 当你配置了event notification的prefix时， 比如estatements/， 他意味着该目录下面的所有的子文件夹中的
指定文件类型的对象创建的时候， 都会触发event notification.  






### python中， list末尾[]加逗号会将其转换成tuple。 差点没笑死我呀



### PLEASE ensure minimum viable product 
