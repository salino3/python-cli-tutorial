# python -m venv venv
# pip install click (virtual enviroment)
# (gitBash) source venv/Scripts/activate


import click
import json_manager

@click.group()
def cli():
    pass


@cli.command()
@click.option('--name', required=True, help='Name of the user')
@click.option('--surname', required=True, help='Surname of the user')
@click.pass_context
def new(ctx, name, surname):
    if not name or not surname:
        ctx.fail("Name and surname are required")
    else:
        data = json_manager.read_json()
        new_id = len(data) + 1
        new_user = {
            'id': new_id,
            'name': name,
            'surname': surname
        }
        data.append(new_user)
        print(data)
        json_manager.write_json(data)
        print(f"User {name} {surname} created successfully with id {new_id}")

     

@cli.command()
def users():
    users = json_manager.read_json()
    for user in users:
        print(f"{user['id']} - {user['name']} - {user['surname']}")


@cli.command
@click.argument('id', type=int)
def user(id):
    data = json_manager.read_json()
    user = next((x for x in data if x['id'] == id), None)
    if user is None:
        print(f"User with id {id} not found")
    else:
        print(f"{user['id']} - {user['name']} - {user['surname']}")



@cli.command
@click.argument('id', type=int) # it does not work as validation
def delete(id):
    data = json_manager.read_json()
    user = next((x for x in data if x['id'] == id), None)
    if user is None:
        print(f"User with id {id} not found")
    else:
        data.remove(user)
        json_manager.write_json(data)
        print(f"User with id {user['id']} deleted successfully")


@cli.command
@click.argument('id', type=int)
@click.option('--name', help="Name of the user")
@click.option('--surname', help="Surname of the user")
def update(id, name, surname):
    data = json_manager.read_json()
    for user in data:
        if user['id'] == id:
            if name is not None:
               user['name'] = name
            if surname is not None:
               user['surname'] = surname
            break
    json_manager.write_json(data)
    print(f"User with id {id} updated successfully")
    





if __name__ == '__main__':
    cli()





