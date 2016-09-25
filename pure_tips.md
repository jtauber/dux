# Tips for keeping Python reducers pure

You can always do a deep copy and then just make the impure manipulation but
this might be inefficient for larger data structures. Here are some
alternatives.

## Appending given item to a list

```
new_list = [*old_list, new_item]
```

## Removing item at given index from a list

```
new_list = old_list[:index] + old_list[index + 1:]
```

## Changing item at given index form a list

```
new_list = old_list[:index] + [change(old_list[index])] + old_list[index + 1:]
```

or

```
new_list = [*old_list[:index], change(old_list[index]), *old_list[index + 1:]]
```

where `change` is a function that gives the new item from the old item.

## adding or changing a key/value in a dict

```
new_dict = {**old_dict, {new_key: new_value}}
```

This can be used to add/change more than one key/value at a time.
