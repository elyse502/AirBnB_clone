<h1 align="center">0x00. AirBnB clone - The console</h1>

```
░█████╗░██╗██████╗░██████╗░███╗░░██╗██████╗░  ░█████╗░██╗░░░░░░█████╗░███╗░░██╗███████╗
██╔══██╗██║██╔══██╗██╔══██╗████╗░██║██╔══██╗  ██╔══██╗██║░░░░░██╔══██╗████╗░██║██╔════╝
███████║██║██████╔╝██████╦╝██╔██╗██║██████╦╝  ██║░░╚═╝██║░░░░░██║░░██║██╔██╗██║█████╗░░
██╔══██║██║██╔══██╗██╔══██╗██║╚████║██╔══██╗  ██║░░██╗██║░░░░░██║░░██║██║╚████║██╔══╝░░
██║░░██║██║██║░░██║██████╦╝██║░╚███║██████╦╝  ╚█████╔╝███████╗╚█████╔╝██║░╚███║███████╗
╚═╝░░╚═╝╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚══╝╚═════╝░  ░╚════╝░╚══════╝░╚════╝░╚═╝░░╚══╝╚══════╝
```

<p align="center">
  <img src="https://github.com/elyse502/AirBnB_clone/assets/125453474/2fa99a64-d82c-4519-b5ad-3c6bf51eb2e9" alt="HolbertonBnB logo">
</p>

<h1 align="center">Alx-HolbertonBnB</h1>
<p align="center">An AirBnB clone.</p>

---

## Description :house:

Alx-HolbertonBnB is a complete web application, integrating database storage, 
a back-end API, and front-end interfacing in a clone of AirBnB.

The project currently only implements the back-end console.

## Classes :cl:

Alx-HolbertonBnB utilizes the following classes:

|     | BaseModel | FileStorage | User | State | City | Amenity | Place | Review |
| --- | --------- | ----------- | -----| ----- | -----| ------- | ----- | ------ |
| **PUBLIC INSTANCE ATTRIBUTES** | `id`<br>`created_at`<br>`updated_at` | | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` |
| **PUBLIC INSTANCE METHODS** | `save`<br>`to_dict` | `all`<br>`new`<br>`save`<br>`reload` | "" | "" | "" | "" | "" | "" |
| **PUBLIC CLASS ATTRIBUTES** | | | `email`<br>`password`<br>`first_name`<br>`last_name`| `name` | `state_id`<br>`name` | `name` | `city_id`<br>`user_id`<br>`name`<br>`description`<br>`number_rooms`<br>`number_bathrooms`<br>`max_guest`<br>`price_by_night`<br>`latitude`<br>`longitude`<br>`amenity_ids` | `place_id`<br>`user_id`<br>`text` | 
| **PRIVATE CLASS ATTRIBUTES** | | `file_path`<br>`objects` | | | | | | |

#### Data Diagram

![99e1a8f2be8c09d5ce5ac321e8cf39f0917f8db5](https://github.com/elyse502/AirBnB_clone/assets/125453474/e833b249-ff9a-4777-bf72-a0e6b6215be7)

## Storage :baggage_claim:

The above classes are handled by the abstracted storage engine defined in the 
[FileStorage](./models/engine/file_storage.py) class.

Every time the backend is initialized, Alx-HolbertonBnB instantiates an instance of 
`FileStorage` called `storage`. The `storage` object is loaded/re-loaded from 
any class instances stored in the JSON file `file.json`. As class instances are 
created, updated, or deleted, the `storage` object is used to register 
corresponding changes in the `file.json`.

## Console :computer:

The console is a command line interpreter that permits management of the backend 
of Alx-HolbertonBnB. It can be used to handle and manipulate all classes utilized by 
the application (achieved by calls on the `storage` object defined above).

### Using the Console

The Alx-HolbertonBnB console can be run both interactively and non-interactively. 
To run the console in non-interactive mode, pipe any command(s) into an execution 
of the file `console.py` at the command line.

```
$ echo "help" | ./console.py
(hbnb) 
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) 
$
```

Alternatively, to use the Alx-HolbertonBnB console in interactive mode, run the 
file `console.py` by itself:

```
$ ./console.py
```

While running in interactive mode, the console displays a prompt for input:

```
$ ./console.py
(hbnb) 
```

To quit the console, enter the command `quit`, or input an EOF signal 
(`ctrl-D`).

```
$ ./console.py
(hbnb) quit
$
```

```
$ ./console.py
(hbnb) EOF
$
```

### Console Commands

The Alx-HolbertonBnB console supports the following commands:

* **create**
  * Usage: `create <class>`

Creates a new instance of a given class. The class' ID is printed and 
the instance is saved to the file `file.json`.

```
$ ./console.py
(hbnb) create BaseModel
5a32fde1-ccb3-496c-9e5c-76530240a506
(hbnb) quit
$ cat file.json ; echo ""
{"BaseModel.eef06f4b-1230-4853-b8c2-08e392c5093d": {"id": "eef06f4b-1230-4853-b8c2-08e392c5093d", "created_at": "2023-08-09T14:13:13.701784", "updated_at": "2023-08-09T14:13:13.701843", "name": "My First Model", "my_number": 89, "__class__": "BaseModel"}, "BaseModel.b9c1473e-c2f7-4739-9d54-20e84865aaba": {"id": "b9c1473e-c2f7-4739-9d54-20e84865aaba", "created_at": "2023-08-09T14:22:43.196665", "updated_at": "2023-08-09T14:22:43.196678", "name": "My_First_Model", "my_number": 89, "__class__": "BaseModel"}, "BaseModel.438a9755-81c1-4a7c-b2aa-fa8b2774bcbf": {"id": "438a9755-81c1-4a7c-b2aa-fa8b2774bcbf", "created_at": "2023-08-09T14:23:20.296687", "updated_at": "2023-08-09T14:23:20.296700", "name": "My_First_Model", "my_number": 89, "__class__": "BaseModel"}, "BaseModel.07d4d83a-982a-4d44-b2e6-f0fbbc3337d1": {"id": "07d4d83a-982a-4d44-b2e6-f0fbbc3337d1", "created_at": "2023-08-09T14:23:45.096648", "updated_at": "2023-08-09T14:23:45.096659", "name": "My_First_Model", "my_number": 89, "__class__": "BaseModel"}, "BaseModel.ec108146-0a45-4f9a-b27f-022acfbe6b3d": {"id": "ec108146-0a45-4f9a-b27f-022acfbe6b3d", "created_at": "2023-08-10T01:36:41.325874", "updated_at": "2023-08-10T01:36:41.325885", "__class__": "BaseModel"}, "User.bf105331-7a3c-4828-a2db-d07f76b69298": {"id": "bf105331-7a3c-4828-a2db-d07f76b69298", "created_at": "2023-08-10T01:41:23.797394", "updated_at": "2023-08-10T01:41:23.797405", "first_name": "Betty", "last_name": "Bar", "email": "airbnb@mail.com", "password": "root", "__class__": "User"}, "User.b54eef30-c8b5-4494-9f05-15a82996a64c": {"id": "b54eef30-c8b5-4494-9f05-15a82996a64c", "created_at": "2023-08-10T01:41:23.797803", "updated_at": "2023-08-10T01:41:23.797814", "first_name": "John", "email": "airbnb2@mail.com", "password": "root", "__class__": "User"}, "User.0b3ee826-d064-48d8-b131-9e5b1ea637e7": {"id": "0b3ee826-d064-48d8-b131-9e5b1ea637e7", "created_at": "2023-08-10T01:42:48.697240", "updated_at": "2023-08-10T01:42:48.697251", "first_name": "Betty", "last_name": "Bar", "email": "airbnb@mail.com", "password": "root", "__class__": "User"}, "User.05c5aa0e-d29d-442f-9891-65d5113bc169": {"id": "05c5aa0e-d29d-442f-9891-65d5113bc169", "created_at": "2023-08-10T01:42:48.697687", "updated_at": "2023-08-10T01:42:48.697698", "first_name": "John", "email": "airbnb2@mail.com", "password": "root", "__class__": "User"}, "BaseModel.5a32fde1-ccb3-496c-9e5c-76530240a506": {"id": "5a32fde1-ccb3-496c-9e5c-76530240a506", "created_at": "2023-08-10T02:34:33.910896", "updated_at": "2023-08-10T02:34:33.910904", "__class__": "BaseModel"}}
```

* **show**
  * Usage: `show <class> <id>` or `<class>.show(<id>)`

Prints the string representation of a class instance based on a given id.

```
$ ./console.py
(hbnb) create User
d874272e-2fd9-4e81-a9f5-9845e0dd494d
(hbnb) 
(hbnb) show User d874272e-2fd9-4e81-a9f5-9845e0dd494d
[User] (d874272e-2fd9-4e81-a9f5-9845e0dd494d) {'id': 'd874272e-2fd9-4e81-a9f5-9845e0dd494d', 'created_at': datetime.datetime(2023, 8, 10, 2, 38, 5, 189631), 'updated_at': datetime.datetime(2023, 8, 10, 2, 38, 5, 189640)}
(hbnb) 
(hbnb)  User.show(d874272e-2fd9-4e81-a9f5-9845e0dd494d)
[User] (d874272e-2fd9-4e81-a9f5-9845e0dd494d) {'id': 'd874272e-2fd9-4e81-a9f5-9845e0dd494d', 'created_at': datetime.datetime(2023, 8, 10, 2, 38, 5, 189631), 'updated_at': datetime.datetime(2023, 8, 10, 2, 38, 5, 189640)}
(hbnb) 
```
* **destroy**
  * Usage: `destroy <class> <id>` or `<class>.destroy(<id>)`

Deletes a class instance based on a given id. The storage file `file.json` 
is updated accordingly.

```
$ ./console.py
(hbnb) create State
d2d789cd-7427-4920-aaae-88cbcf8bffe2
(hbnb) create Place
3e-8329-4f47-9947-dca80c03d3ed
(hbnb)
(hbnb) destroy State d2d789cd-7427-4920-aaae-88cbcf8bffe2
(hbnb) Place.destroy(03486a3e-8329-4f47-9947-dca80c03d3ed)
(hbnb) quit
$ cat file.json ; echo ""
{}
```

* **all**
  * Usage: `all` or `all <class>` or `<class>.all()`

Prints the string representations of all instances of a given class. If no 
class name is provided, the command prints all instances of every class.

```
$ ./console.py
(hbnb) create BaseModel
b4cd1fe5-dbe2-4af9-be93-861737eb2116
(hbnb) create BaseModel
3e883e3e-de65-4471-b25e-441ee917b7d8
(hbnb) create User
57a356c8-9310-402a-82e6-9646b5f98eca
(hbnb) create User
6b406424-8830-4821-8788-7f7b776fd9d4
(hbnb)
(hbnb) all BaseModel
["[BaseModel] (eef06f4b-1230-4853-b8c2-08e392c5093d) {'id': 'eef06f4b-1230-4853-b8c2-08e392c5093d', 'created_at': datetime.datetime(2023, 8, 9, 14, 13, 13, 701784), 'updated_at': datetime.datetime(2023, 8, 9, 14, 13, 13, 701843), 'name': 'My First Model', 'my_number': 89}", "[BaseModel] (b9c1473e-c2f7-4739-9d54-20e84865aaba) {'id': 'b9c1473e-c2f7-4739-9d54-20e84865aaba', 'created_at': datetime.datetime(2023, 8, 9, 14, 22, 43, 196665), 'updated_at': datetime.datetime(2023, 8, 9, 14, 22, 43, 196678), 'name': 'My_First_Model', 'my_number': 89}", "[BaseModel] (438a9755-81c1-4a7c-b2aa-fa8b2774bcbf) {'id': '438a9755-81c1-4a7c-b2aa-fa8b2774bcbf', 'created_at': datetime.datetime(2023, 8, 9, 14, 23, 20, 296687), 'updated_at': datetime.datetime(2023, 8, 9, 14, 23, 20, 296700), 'name': 'My_First_Model', 'my_number': 89}", "[BaseModel] (07d4d83a-982a-4d44-b2e6-f0fbbc3337d1) {'id': '07d4d83a-982a-4d44-b2e6-f0fbbc3337d1', 'created_at': datetime.datetime(2023, 8, 9, 14, 23, 45, 96648), 'updated_at': datetime.datetime(2023, 8, 9, 14, 23, 45, 96659), 'name': 'My_First_Model', 'my_number': 89}", "[BaseModel] (ec108146-0a45-4f9a-b27f-022acfbe6b3d) {'id': 'ec108146-0a45-4f9a-b27f-022acfbe6b3d', 'created_at': datetime.datetime(2023, 8, 10, 1, 36, 41, 325874), 'updated_at': datetime.datetime(2023, 8, 10, 1, 36, 41, 325885)}", "[BaseModel] (5a32fde1-ccb3-496c-9e5c-76530240a506) {'id': '5a32fde1-ccb3-496c-9e5c-76530240a506', 'created_at': datetime.datetime(2023, 8, 10, 2, 34, 33, 910896), 'updated_at': datetime.datetime(2023, 8, 10, 2, 34, 33, 910904)}", "[BaseModel] (b4cd1fe5-dbe2-4af9-be93-861737eb2116) {'id': 'b4cd1fe5-dbe2-4af9-be93-861737eb2116', 'created_at': datetime.datetime(2023, 8, 10, 2, 56, 52, 589426), 'updated_at': datetime.datetime(2023, 8, 10, 2, 56, 52, 589434)}", "[BaseModel] (3e883e3e-de65-4471-b25e-441ee917b7d8) {'id': '3e883e3e-de65-4471-b25e-441ee917b7d8', 'created_at': datetime.datetime(2023, 8, 10, 2, 57, 2, 396120), 'updated_at': datetime.datetime(2023, 8, 10, 2, 57, 2, 396127)}"]
(hbnb)
(hbnb) User.all()
["[User] (bf105331-7a3c-4828-a2db-d07f76b69298) {'id': 'bf105331-7a3c-4828-a2db-d07f76b69298', 'created_at': datetime.datetime(2023, 8, 10, 1, 41, 23, 797394), 'updated_at': datetime.datetime(2023, 8, 10, 1, 41, 23, 797405), 'first_name': 'Betty', 'last_name': 'Bar', 'email': 'airbnb@mail.com', 'password': 'root'}", "[User] (b54eef30-c8b5-4494-9f05-15a82996a64c) {'id': 'b54eef30-c8b5-4494-9f05-15a82996a64c', 'created_at': datetime.datetime(2023, 8, 10, 1, 41, 23, 797803), 'updated_at': datetime.datetime(2023, 8, 10, 1, 41, 23, 797814), 'first_name': 'John', 'email': 'airbnb2@mail.com', 'password': 'root'}", "[User] (0b3ee826-d064-48d8-b131-9e5b1ea637e7) {'id': '0b3ee826-d064-48d8-b131-9e5b1ea637e7', 'created_at': datetime.datetime(2023, 8, 10, 1, 42, 48, 697240), 'updated_at': datetime.datetime(2023, 8, 10, 1, 42, 48, 697251), 'first_name': 'Betty', 'last_name': 'Bar', 'email': 'airbnb@mail.com', 'password': 'root'}", "[User] (05c5aa0e-d29d-442f-9891-65d5113bc169) {'id': '05c5aa0e-d29d-442f-9891-65d5113bc169', 'created_at': datetime.datetime(2023, 8, 10, 1, 42, 48, 697687), 'updated_at': datetime.datetime(2023, 8, 10, 1, 42, 48, 697698), 'first_name': 'John', 'email': 'airbnb2@mail.com', 'password': 'root'}", "[User] (d874272e-2fd9-4e81-a9f5-9845e0dd494d) {'id': 'd874272e-2fd9-4e81-a9f5-9845e0dd494d', 'created_at': datetime.datetime(2023, 8, 10, 2, 38, 5, 189631), 'updated_at': datetime.datetime(2023, 8, 10, 2, 38, 5, 189640)}", "[User] (57a356c8-9310-402a-82e6-9646b5f98eca) {'id': '57a356c8-9310-402a-82e6-9646b5f98eca', 'created_at': datetime.datetime(2023, 8, 10, 2, 57, 15, 97735), 'updated_at': datetime.datetime(2023, 8, 10, 2, 57, 15, 97745)}", "[User] (6b406424-8830-4821-8788-7f7b776fd9d4) {'id': '6b406424-8830-4821-8788-7f7b776fd9d4', 'created_at': datetime.datetime(2023, 8, 10, 2, 57, 32, 397213), 'updated_at': datetime.datetime(2023, 8, 10, 2, 57, 32, 397221)}"]
(hbnb) 
(hbnb) all
["[BaseModel] (eef06f4b-1230-4853-b8c2-08e392c5093d) {'id': 'eef06f4b-1230-4853-b8c2-08e392c5093d', 'created_at': datetime.datetime(2023, 8, 9, 14, 13, 13, 701784), 'updated_at': datetime.datetime(2023, 8, 9, 14, 13, 13, 701843), 'name': 'My First Model', 'my_number': 89}", "[BaseModel] (b9c1473e-c2f7-4739-9d54-20e84865aaba) {'id': 'b9c1473e-c2f7-4739-9d54-20e84865aaba', 'created_at': datetime.datetime(2023, 8, 9, 14, 22, 43, 196665), 'updated_at': datetime.datetime(2023, 8, 9, 14, 22, 43, 196678), 'name': 'My_First_Model', 'my_number': 89}", "[BaseModel] (438a9755-81c1-4a7c-b2aa-fa8b2774bcbf) {'id': '438a9755-81c1-4a7c-b2aa-fa8b2774bcbf', 'created_at': datetime.datetime(2023, 8, 9, 14, 23, 20, 296687), 'updated_at': datetime.datetime(2023, 8, 9, 14, 23, 20, 296700), 'name': 'My_First_Model', 'my_number': 89}", "[BaseModel] (07d4d83a-982a-4d44-b2e6-f0fbbc3337d1) {'id': '07d4d83a-982a-4d44-b2e6-f0fbbc3337d1', 'created_at': datetime.datetime(2023, 8, 9, 14, 23, 45, 96648), 'updated_at': datetime.datetime(2023, 8, 9, 14, 23, 45, 96659), 'name': 'My_First_Model', 'my_number': 89}", "[BaseModel] (ec108146-0a45-4f9a-b27f-022acfbe6b3d) {'id': 'ec108146-0a45-4f9a-b27f-022acfbe6b3d', 'created_at': datetime.datetime(2023, 8, 10, 1, 36, 41, 325874), 'updated_at': datetime.datetime(2023, 8, 10, 1, 36, 41, 325885)}", "[User] (bf105331-7a3c-4828-a2db-d07f76b69298) {'id': 'bf105331-7a3c-4828-a2db-d07f76b69298', 'created_at': datetime.datetime(2023, 8, 10, 1, 41, 23, 797394), 'updated_at': datetime.datetime(2023, 8, 10, 1, 41, 23, 797405), 'first_name': 'Betty', 'last_name': 'Bar', 'email': 'airbnb@mail.com', 'password': 'root'}", "[User] (b54eef30-c8b5-4494-9f05-15a82996a64c) {'id': 'b54eef30-c8b5-4494-9f05-15a82996a64c', 'created_at': datetime.datetime(2023, 8, 10, 1, 41, 23, 797803), 'updated_at': datetime.datetime(2023, 8, 10, 1, 41, 23, 797814), 'first_name': 'John', 'email': 'airbnb2@mail.com', 'password': 'root'}", "[User] (0b3ee826-d064-48d8-b131-9e5b1ea637e7) {'id': '0b3ee826-d064-48d8-b131-9e5b1ea637e7', 'created_at': datetime.datetime(2023, 8, 10, 1, 42, 48, 697240), 'updated_at': datetime.datetime(2023, 8, 10, 1, 42, 48, 697251), 'first_name': 'Betty', 'last_name': 'Bar', 'email': 'airbnb@mail.com', 'password': 'root'}", "[User] (05c5aa0e-d29d-442f-9891-65d5113bc169) {'id': '05c5aa0e-d29d-442f-9891-65d5113bc169', 'created_at': datetime.datetime(2023, 8, 10, 1, 42, 48, 697687), 'updated_at': datetime.datetime(2023, 8, 10, 1, 42, 48, 697698), 'first_name': 'John', 'email': 'airbnb2@mail.com', 'password': 'root'}", "[BaseModel] (5a32fde1-ccb3-496c-9e5c-76530240a506) {'id': '5a32fde1-ccb3-496c-9e5c-76530240a506', 'created_at': datetime.datetime(2023, 8, 10, 2, 34, 33, 910896), 'updated_at': datetime.datetime(2023, 8, 10, 2, 34, 33, 910904)}", "[User] (d874272e-2fd9-4e81-a9f5-9845e0dd494d) {'id': 'd874272e-2fd9-4e81-a9f5-9845e0dd494d', 'created_at': datetime.datetime(2023, 8, 10, 2, 38, 5, 189631), 'updated_at': datetime.datetime(2023, 8, 10, 2, 38, 5, 189640)}", "[Place] (99e06c20-70f9-40fc-8e86-cd7f4ad00b4f) {'id': '99e06c20-70f9-40fc-8e86-cd7f4ad00b4f', 'created_at': datetime.datetime(2023, 8, 10, 2, 52, 21, 686662), 'updated_at': datetime.datetime(2023, 8, 10, 2, 52, 21, 686672)}", "[State] (8ddd037b-b5e1-42f7-921d-f13a6d56973b) {'id': '8ddd037b-b5e1-42f7-921d-f13a6d56973b', 'created_at': datetime.datetime(2023, 8, 10, 2, 54, 2, 964557), 'updated_at': datetime.datetime(2023, 8, 10, 2, 54, 2, 964565)}", "[Place] (4943685b-72d0-48a5-9a80-8e726dafd2d1) {'id': '4943685b-72d0-48a5-9a80-8e726dafd2d1', 'created_at': datetime.datetime(2023, 8, 10, 2, 54, 26, 644304), 'updated_at': datetime.datetime(2023, 8, 10, 2, 54, 26, 644313)}", "[BaseModel] (b4cd1fe5-dbe2-4af9-be93-861737eb2116) {'id': 'b4cd1fe5-dbe2-4af9-be93-861737eb2116', 'created_at': datetime.datetime(2023, 8, 10, 2, 56, 52, 589426), 'updated_at': datetime.datetime(2023, 8, 10, 2, 56, 52, 589434)}", "[BaseModel] (3e883e3e-de65-4471-b25e-441ee917b7d8) {'id': '3e883e3e-de65-4471-b25e-441ee917b7d8', 'created_at': datetime.datetime(2023, 8, 10, 2, 57, 2, 396120), 'updated_at': datetime.datetime(2023, 8, 10, 2, 57, 2, 396127)}", "[User] (57a356c8-9310-402a-82e6-9646b5f98eca) {'id': '57a356c8-9310-402a-82e6-9646b5f98eca', 'created_at': datetime.datetime(2023, 8, 10, 2, 57, 15, 97735), 'updated_at': datetime.datetime(2023, 8, 10, 2, 57, 15, 97745)}", "[User] (6b406424-8830-4821-8788-7f7b776fd9d4) {'id': '6b406424-8830-4821-8788-7f7b776fd9d4', 'created_at': datetime.datetime(2023, 8, 10, 2, 57, 32, 397213), 'updated_at': datetime.datetime(2023, 8, 10, 2, 57, 32, 397221)}"]
(hbnb) 
```

* **count**
  * Usage: `count <class>` or `<class>.count()`

Retrieves the number of instances of a given class.

```
$ ./console.py
(hbnb) create Place
12c73223-f3d3-4dec-9629-bd19c8fadd8a
(hbnb) create Place
aa229cbb-5b19-4c32-8562-f90a3437d301
(hbnb) create City
22a51611-17bd-4d8f-ba1b-3bf07d327208
(hbnb) 
(hbnb) count Place
2
(hbnb) city.count()
1
(hbnb) 
```

* **update**
  * Usage: `update <class> <id> <attribute name> "<attribute value>"` or
`<class>.update(<id>, <attribute name>, <attribute value>)` or `<class>.update(
<id>, <attribute dictionary>)`.

Updates a class instance based on a given id with a given key/value attribute 
pair or dictionary of attribute pairs. If `update` is called with a single 
key/value attribute pair, only "simple" attributes can be updated (ie. not 
`id`, `created_at`, and `updated_at`). However, any attribute can be updated by 
providing a dictionary.

```
$ ./console.py
(hbnb) create User
33478803-5242-4f95-b254-b770ef4d335e
(hbnb)
(hbnb) update User 33478803-5242-4f95-b254-b770ef4d335e first_name "Best"
(hbnb) show User 33478803-5242-4f95-b254-b770ef4d335e
[User] (33478803-5242-4f95-b254-b770ef4d335e) {'id': '33478803-5242-4f95-b254-b770ef4d335e', 'created_at': datetime.datetime(2023, 8, 10, 4, 18, 43, 58659), 'updated_at': datetime.datetime(2023, 8, 10, 4, 18, 43, 58669), 'first_name': 'Best'}
(hbnb)
(hbnb) User.update(33478803-5242-4f95-b254-b770ef4d335e, address, "KK 806 St")
(hbnb) User.show(33478803-5242-4f95-b254-b770ef4d335e)
[User] (33478803-5242-4f95-b254-b770ef4d335e) {'id': '33478803-5242-4f95-b254-b770ef4d335e', 'created_at': datetime.datetime(2023, 8, 10, 4, 18, 43, 58659), 'updated_at': datetime.datetime(2023, 8, 10, 4, 18, 43, 58669), 'first_name': 'Best', 'address': 'KK 806 St'}
(hbnb)
(hbnb) User.update(6f348019-0499-420f-8eec-ef0fdc863c02, {'email': 'airbnb@mail.com', 'last_name': 'School'})
(hbnb) show User 33478803-5242-4f95-b254-b770ef4d335e
[User] (33478803-5242-4f95-b254-b770ef4d335e) {'id': '33478803-5242-4f95-b254-b770ef4d335e', 'created_at': datetime.datetime(2023, 8, 10, 4, 18, 43, 58659), 'updated_at': datetime.datetime(2023, 8, 10, 4, 18, 43, 58669), 'first_name': 'Best', 'address': '98 Mission St', 'email': 'airbnb@mail.com', 'last_name': 'School'}
(hbnb) 
```

## Testing :straight_ruler:

Unittests for the Alx-HolbertonBnB project are defined in the [tests](./tests) 
folder. To run the entire test suite simultaneously, execute the following command:

```
$ python3 -m unittest discover tests
```

Alternatively, you can specify a single test file to run at a time:

```
$ python3 -m unittest tests/test_console.py
```

## Authors :black_nib:
1. _[NIYIBIZI Elysée](https://mail.google.com/mail/u/0/#inbox) | [Github](https://github.com/elyse502) | [Linkedin](https://www.linkedin.com/in/niyibizi-elys%C3%A9e/) | [Twitter](https://twitter.com/Niyibizi_Elyse)._
2. _Joseph Kimuchu | [Github](https://github.com/KimuchuJr) | [Linkedin](https://www.linkedin.com/in/joseph-kimuchu-2a6031224/)._

## Acknowledgements 🤝
All work contained in this project was completed as part of the curriculum for Alx-Holberton School. Alx-Holberton School is a Remote-based full-stack software engineering program that prepares students for careers in the tech industry using project-based peer learning. For more information, visit [This link](https://www.alxafrica.com/).

<p align="center">
<h2 align="center"><img align="center" src="https://github.com/elyse502/AirBnB_clone/assets/125453474/ab3c1e01-2b98-47ae-96b7-37c07c85a2f1" alt="footer" width="150"  height="150"/></h2>
