def parser(args, actions):
    for action in actions:
        if args.get(action):
            return actions[action](**args)
    raise NotImplemented


class NotImplemented:
    pass
