# Design Patterns Rooom Management

## About

This repository is used to try out different design patterns identified by <cite>Gamma et al. (1995)</cite> [1]. A prototype room management system was developed for this purpose. The usage is demonstrated in <b>run.ipynb</b>.

## Used Design Patterns

### Builder Pattern

The `BuildingDatabaseManager` class acts as a builder class that performs manipulations on the `BuildingDatabase` class which represents the database with all informations, including (listed in the next section). The `BuildingDatabaseManager` class provides methods to the outside for this purpose.

### Factory Pattern

The Factory pattern was used to easily create different parts. These are the following parts (represented as Classes): `Building`, `BuildingPart`, `Room`, `Hallway`, `Stairway`. New objects of these are created by the `BuildingFactory` which acts as a factory. The `BuildingFactory` is used by the `BuildingDatabaseManager` like that:

```python
new_building = BuildingFactory.create_part(part_type="building", id="B-1", faculty="Computer Science")
```

The new building will then be an instance of the `Building` class.

### Service Pattern

The strategy pattern was demonstrated by a prototypical authentication. Users can select between the two strategies `LoginAccountStrategy` and `LoginAccountStrategyTwoFactor`. The selected Strategy needs to be passed like that:

```python
building_database_manager = BuildingDatabaseManager(LoginAccountStrategy())
```

Just replace the instance of 'LoginAccountStrategy' with the desired strategy. It is also possible to create new strategies besides the two.

## Literature

[1] Gamma, E., Helm, R., Johnson, R., Johnson, R. E., & Vlissides, J. (1995). Design patterns: elements of reusable object-oriented software. Pearson Deutschland GmbH.
