import ReadFile as RF
import CycleCancelingAlgorithm as CC


def main():
    file_path = 'sample01.txt'
    item_lists = RF.read_item_lists_from_file(file_path)
    CC.trade_maximizer_with_cycle_canceling_algorthm(item_lists)


if __name__ == "__main__":
    main()
