git clone -b carlos.gonzalez/add-custom-metric-command https://github.com/DataDog/datadog-ci.git

cd datadog-ci

yarn install
yarn launch tag --level pipeline --tags team:ci-app
yarn launch tag --level job --tags foo:bar
