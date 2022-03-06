#!/usr/bin/python3
""" Script to list all states in a database """


if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                sys.argv[1],
                sys.argv[2],
                sys.argv[3]),
            pool_pre_ping=True
            )

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()
    states = session.query(State).filter(State.name == sys.argv[4]).all()
    # states = session.query(State).all()

    if len(states) != 0:
        for state in list(states):
            print(str(state.id))
    else:
        print('Not found')
