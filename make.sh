abcd() {
    echo 1
}

# get_current_file_directory() {
#     file_abs_path="$(readlink -f "${BASH_SOURCE[0]}")"
#     directory_path="$(dirname "${file_abs_path}")"
#     echo "${directory_path}"
# }

# for i in ./foo.sh;
# do
#     source $i
# done
source foo.sh
# get_current_file_directory


help() {
    cat ${BASH_SOURCE[0]}
}

"$@"
