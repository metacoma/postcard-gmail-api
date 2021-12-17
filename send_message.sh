#!/bin/sh

# ./send_message.sh -n 'John Connor' -e 'johnconnergmail.com' -c "XXX-YYY-XXX"

NAME=$1
CODE=$2
EMAIL=$3

usage() { echo "Usage: $0 [-n name] [-c code] [-e email]" 1>&2; exit 1; }

while getopts ":n:c:e:" o; do
    case "${o}" in
        n)
            name=${OPTARG}
            ;;
        c)
            code=${OPTARG}
            ;;
        e)
            email=${OPTARG}
            ;;
        *)
            usage
            ;;
    esac
done
shift $((OPTIND-1))

if [ -z "${name}" ] || [ -z "${code}" ] || [ -z "${email}" ]; then
    usage
fi

echo "name = ${name}"
echo "code = ${code}"
echo "email = ${email}"

IMG_TMP=`mktemp /tmp/certXXXXXXXXXXX.png`

./convert.sh "$name" > $IMG_TMP
. .venv/bin/activate
python ./send_mesasge.py "$email" "$code" "$IMG_TMP"
