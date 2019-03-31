dropDB_cmd="python manage.py migrate learningmodule zero"
eval $dropDB_cmd

changeDir="cd learningmodule"

eval $changeDir

remove_mig_files="rm -r migrations"

eval $remove_mig_files

changeDir="cd .."

eval $changeDir

create_MIG_files="python manage.py makemigrations learningmodule"

eval $create_MIG_files

createDB="python manage.py migrate"

eval $createDB

