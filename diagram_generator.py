from sqlalchemy_schemadisplay import create_schema_graph
from sqlalchemy import MetaData

def main():
    graph = create_schema_graph(metadata=MetaData('postgresql://student:student@127.0.0.1/sparkifydb'),
                               show_datatypes=False, show_indexes=False, rankdir='=LR', concentrate=True)
    graph.write_png('test.png')

if __name__ == "__main__":
    main()