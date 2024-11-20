from app.db.database import get_db

from app.core.security import hash_password

from app.models.user import User
from app.models.worlds import World
from app.models.members import WorldMember
from app.models.channels import Channel
from app.models.messages import Message

database = next(get_db())
print(database)

# Create a couple of users
test_user = User(
    username="system",
    email="test@test.dev",
    password=hash_password("test"),
)

another_user = User(
    username="partner",
    email="another@another.dev",
    password=hash_password("test")
)

database.add(test_user)
database.add(another_user)
database.commit()
database.refresh(test_user)
database.refresh(another_user)

# Create a sample world with the test user as the owner
test_world = World(
    name="Hello, world!",
    description="This is a sample world for testing. Have fun! :P",
    owner_id=test_user.id
)

# Create a test personal chat between `s` and `another` users
test_chat = World(
    name="IGNORE CHAT NAME",
    description="This is a personal chat!",
    owner_id=test_user.id,
    is_personal_chat=True
)

database.add(test_world)
database.add(test_chat)
database.commit()
database.refresh(test_world)
database.refresh(test_chat)

# Add memberships
test_world_test_member = WorldMember(
    world_id=test_world.id,
    user_id=test_user.id,
    role="owner"
)

test_world_another_member = WorldMember(
    world_id=test_world.id,
    user_id=another_user.id,
    role="member"
)

test_chat_test_member = WorldMember(
    world_id=test_chat.id,
    user_id=test_user.id,
    role="owner"
)

test_chat_another_member = WorldMember(
    world_id=test_chat.id,
    user_id=another_user.id,
    role="owner"
)

database.add(test_world_test_member)
database.add(test_world_another_member)
database.add(test_chat_test_member)
database.add(test_chat_another_member)
database.commit()

# Add a test channel to the regular world
test_channel = Channel(
    name="A text channel",
    type="text",
    world_id=test_world.id
)

database.add(test_channel)
database.commit()
database.refresh(test_channel)

# Add some messages to the test channel
m1 = Message(
    channel_id=test_channel.id,
    user_id=test_user.id,
    content="Hello, everyone! This is the very first message in this world!"
)
m2 = Message(
    channel_id=test_channel.id,
    user_id=another_user.id,
    content="Man, fuck off! Stop with the grand messages!"
)
m3 = Message(
    channel_id=test_channel.id,
    user_id=test_user.id,
    content="Sorry, but hate speech is not tolerated here!"
)
m4 = Message(
    channel_id=test_channel.id,
    user_id=test_user.id,
    content="I am banning you!"
)
m5 = Message(
    channel_id=test_channel.id,
    user_id=test_user.id,
    content="Oh, wait..."
)
m6 = Message(
    channel_id=test_channel.id,
    user_id=test_user.id,
    content="I can't :o"
)
m7 = Message(
    channel_id=test_channel.id,
    user_id=another_user.id,
    content="Ha-ha! :D"
)

database.add(m1)
database.add(m2)
database.add(m3)
database.add(m4)
database.add(m5)
database.add(m6)
database.add(m7)
database.commit()