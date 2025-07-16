from argparse_dataclass import dataclass,ArgumentParser
@dataclass
class Options:
    data_dir: str = "/home/tangyuan/project/car_segment_"
    output_dir: str = "/home/tangyuan/project/car_segment_wjq"

parser = ArgumentParser(Options)
args = parser.parse_args()