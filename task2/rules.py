

actionList = ['Drink', 'Eat', 'MoveRight', 'MoveLeft']


table = {
     (('A', 'MilkHere'),): 'Drink',
    (('A', 'SausageHere'),): 'Eat',
    (('B', 'MilkHere'),): 'Drink',
    (('B', 'SausageHere'),): 'Eat',

    #not really needed since itll never be empty
    (('A', 'Empty'),): 'MoveRight', 
    (('B', 'Empty'),): 'MoveLeft',  

    # Start at A mvoed to B, consumed it
    (('A', 'MilkHere'), ('A', 'Empty')): 'MoveRight',
    (('A', 'SausageHere'), ('A', 'Empty')): 'MoveRight',
    
    # Start at B mvoed to A, consumed it
    (('B', 'MilkHere'), ('B', 'Empty')): 'MoveLeft',
    (('B', 'SausageHere'), ('B', 'Empty')): 'MoveLeft',

    #from room A to B
    (('A', 'MilkHere'), ('A', 'Empty'), ('B', 'SausageHere')): 'Eat',
    (('A', 'SausageHere'), ('A', 'Empty'), ('B', 'SausageHere')): 'Eat',
    (('A', 'MilkHere'), ('A', 'Empty'), ('B', 'MilkHere')): 'Drink',
    (('A', 'SausageHere'), ('A', 'Empty'), ('B', 'MilkHere')): 'Drink',
    
    #From room B to A
    (('B', 'SausageHere'), ('B', 'Empty'), ('A', 'MilkHere')): 'Drink',
    (('B', 'MilkHere'), ('B', 'Empty'), ('A', 'MilkHere')): 'Drink',
    (('B', 'SausageHere'), ('B', 'Empty'), ('A', 'SausageHere')): 'Eat',
    (('B', 'MilkHere'), ('B', 'Empty'), ('A', 'SausageHere')): 'Eat',
    
    
    #empty both rooms
    (('A', 'MilkHere'), ('A', 'Empty'), ('B', 'SausageHere'), ('B', 'Empty')): None,
    (('A', 'SausageHere'), ('A', 'Empty'), ('B', 'MilkHere'), ('B', 'Empty')): None,
    (('B', 'MilkHere'), ('B', 'Empty'), ('A', 'SausageHere'), ('A', 'Empty')): None,
    (('B', 'SausageHere'), ('B', 'Empty'), ('A', 'MilkHere'), ('A', 'Empty')): None,
}

