git clone -b carlos.gonzalez/add-custom-tags-command https://github.com/DataDog/datadog-ci.git

cd datadog-ci

yarn install
yarn launch tag --level pipeline --tags team:ci-app
