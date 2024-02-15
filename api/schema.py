from tortoise.models import Model
from tortoise import fields, run_async, Tortoise 
from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator

class User(Model):
    id = fields.IntField(pk=True, index= True)
    name = fields.CharField(max_length=20)
    password = fields.CharField(max_length= 200)
    description = fields.CharField(max_length=100)

    posts: fields.ReverseRelation["Post"]

class Post(Model):
    id = fields.CharField(pk=True,max_length=50, index =True)
    title = fields.CharField(max_length=100)
    # created_by = fields.CharField(max_length=20)
    # created_at = fields.DatetimeField()
    
    user: fields.ForeignKeyRelation["User"]= fields.ForeignKeyField(
        "models.User", related_name="posts", description="The user created posts "
    )
 
User_Pydantic = pydantic_model_creator(User)

async def connectToDatabase(create_db=False):
    await Tortoise.init(
        db_url='sqlite://posts.db',
        modules={'models': ['__main__']}
    )
    
    if create_db:
        # Uncomment this to initialize db. 
        await Tortoise.generate_schemas()
    

if __name__ == "__main__":
    run_async(connectToDatabase(create_db=False))