# kun.uz

## Api documentation

### data base sxema

![alt text](kun_uz_img.png)

# `Home api`

| Method | Path | Description |
| ------ | ------ | ------ |
| GET | `kun_uz/` | Get home page data |



# `Area new api`

| Method | Path | Description |
| ------ | ------ | ------ |
| POST | `kun_uz/area/create/` | Create area new |
| POST | `kun_uz/area/update/<int:pk>/` | Update area new |
| POST | `kun_uz/area/delete/<int:pk>/` | Delete area new by id |
| GET | `kun_uz/area/list/` | Get all area news |
| GET | `kun_uz/area/detail/<int:pk>/` | Get area new by id |


# `News api`

| Method | Path | Description |
| ------ | ------ | ------ |
| POST | `kun_uz/new_type/create/` | Create new type |
| POST | `kun_uz/new_type/update/<int:pk>/` | Update type |
| GET | `kun_uz/new_type/list/` | Get all types |
| GET | `kun_uz/new_type/detail/<int:pk>/` | Get type by id |
| POST | `kun_uz/new_type/delete/<int:pk>/` | Delete type by id |


# `Day new api`

| Method | Path | Description |
| ------ | ------ | ------ |
| POST | `kun_uz/day_new/create/` | Create day new |
| POST | `kun_uz/day_new/update/<int:pk>/` | Update day new |
| GET | `kun_uz/day_new/list/` | Get all day news |
| GET | `kun_uz/day_new/detail/<int:pk>/` | Get day new by id |
| POST | `kun_uz/day_new/delete/<int:pk>/` | Delete day new by id |

# `Actual new api`

| Method | Path | Description |
| ------ | ------ | ------ |
| POST | `kun_uz/actual/create/` | Create actual new |
| POST | `kun_uz/actual/update/<int:pk>/` | Update actual new |
| GET | `kun_uz/actual/list/` | Get all actual news |
| POST | `kun_uz/actual/delete/<int:pk>/` | Delete actual new by id |

# `Intervyu api`

| Method | Path | Description |
| ------ | ------ | ------ |
| POST | `kun_uz/intervyu/create/` | Create intervyu |
| POST | `kun_uz/intervyu/update/<int:pk>/` | Update intervyu |
| GET | `kun_uz/intervyu/list/` | Get all intervyus |
| GET | `kun_uz/intervyu/detail/list_all/` | Get all intervyus with all fields |
| GET | `kun_uz/intervyu/detail/<int:pk>/` | Get intervyu by id |
| POST | `kun_uz/intervyu/delete/<int:pk>/` | Delete intervyu by id |

# `Article api`

| Method | Path | Description |
| ------ | ------ | ------ |
| POST | `kun_uz/article/create/` | Create article |
| POST | `kun_uz/article/update/<int:pk>/` | Update article |
| POST | `kun_uz/article/delete/<int:pk>/` | Delete article by id |
| GET | `kun_uz/article/list/` | Get all articles |
| GET | `kun_uz/article/detail/list_all/` | Get all articles with all fields |
| GET | `kun_uz/article/detail/<int:pk>/` | Get article by id |

# `Bisnes new api`

| Method | Path | Description |
| ------ | ------ | ------ |
| POST | `kun_uz/bisnes_new/create/` | Create bisnes new |
| POST | `kun_uz/bisnes_new/update/<int:pk>/` | Update bisnes new |
| POST | `kun_uz/bisnes_new/delete/<int:pk>/` | Delete bisnes new by id |
| GET | `kun_uz/bisnes_new/list_all/` | Get all bisnes news with all fields |
| GET | `kun_uz/bisnes_new/detail/<int:pk>/` | Get bisnes new by id |



