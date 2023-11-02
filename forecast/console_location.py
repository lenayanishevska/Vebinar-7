from weather_forecast import get_forecast
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--text', type=str, help='City')
    args = parser.parse_args()

    if args.text:
        get_forecast(args.text)
    else:
        print('No city parameter')


if __name__ == '__main__':
    main()