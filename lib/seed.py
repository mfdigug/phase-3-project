from models import create_engine, session, Customer, MenuItem, Mod, OrderItem, Order

if __name__ == '__main__':

    engine = create_engine('sqlite:///seed_db.db')

    session.query(Game).delete()
    session.commit()

    botw = Game(title="Breath of the Wild", platform="Switch",
                genre="Adventure", price=60)
    ffvii = Game(title="Final Fantasy VII",
                 platform="Playstation", genre="RPG", price=30)
    mk8 = Game(title="Mario Kart 8", platform="Switch",
               genre="Racing", price=50)
    ccs = Game(title="Candy Crush Saga",
               platform="Mobile", genre="Puzzle", price=0)

    session.add_all([botw, ffvii, mk8, ccs])
    session.commit()
