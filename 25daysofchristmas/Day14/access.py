import boto3
s3 = boto3.client('s3')
# s3 = boto3.client('s3')
# obj = s3.get_object(Bucket='advent-bucket-one')
# li = s3.list_objects(Bucket='advent-bucket-one')['Contents']
# for key in li:
#     print(key)

obj = s3.get_object(Bucket='advent-bucket-one', Key="employee_names.txt")
file_content = (line.decode('utf-8') for line in obj['Body'].iter_lines())
for line in file_content:
    print(line)