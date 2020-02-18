$scope.getZones = function (data) {
    // console.log(data)
    if (data.state_code != "" && data.state_code != undefined) {
        var kwargs = {

            "query_type": "get_zones",
            "state_code": "1"
        }
        BlankFactory.getLocationChildrens(kwargs, $scope.django_csrf_token).then(function (response) {
            if (response.success) {

                $scope.zonesList = response['data'];
                console.log($scope.zonesList)
                $scope.districtlist = [];
                $scope.divisionlist = [];
                $scope.helthblockdata = [];
                $scope.helthfacilitydata = [];
                $scope.helthsubfacilitydata = [];
                $scope.villagedata = []

                $scope.rg.district_code = "All";
                $scope.rg.division_code = "All"
                $scope.rg.block_code = "All";
                $scope.rg.facility_code = "All";
                $scope.rg.subfacility_code = "All";
                $scope.rg.village_code = "All";
            }
        })
    }
    else {
        $scope.zonesList = []
        $scope.districtlist = []
        $scope.divisionlist = [];
        $scope.helthblockdata = [];
        $scope.helthfacilitydata = [];
        $scope.helthsubfacilitydata = [];
        $scope.villagedata = []

        $scope.rg.district_code = "All";
        $scope.rg.division_code = "All"
        $scope.rg.block_code = "All";
        $scope.rg.facility_code = "All";
        $scope.rg.subfacility_code = "All";
        $scope.rg.village_code = "All";
    }
}
$scope.getZones($scope.rg)
// $scope.loadDistricts();

// calling Districts

$scope.getDistricts = function (data) {
    if (data.zone_code != 'All') {
        var kwargs = {
            "query_type": "get_districts",
            "state_code": $scope.rg.state_code,
            "zone_code": $scope.rg.zone_code
        }
        BlankFactory.getLocationChildrens(kwargs, $scope.django_csrf_token).then(function (response) {
            if (response.success) {

                $scope.districtlist = response['data'];
                console.log($scope.districtlist)
                $scope.divisionlist = $scope.helthblockdata = $scope.helthfacilitydata = $scope.helthsubfacilitydata = $scope.villagedata = [];
                $scope.rg.district_code = "All";
                $scope.rg.block_code = "All";
                $scope.rg.facility_code = "All";
                $scope.rg.subfacility_code = "All";
                $scope.rg.village_code = "All";

            }
        })
    }
    else {

        $scope.districtlist = $scope.divisionlist = $scope.helthblockdata = $scope.helthfacilitydata = $scope.helthsubfacilitydata = $scope.villagedata = [];
        $scope.rg.district_code = $scope.rg.division_code = $scope.rg.block_code = $scope.rg.facility_code = $scope.rg.subfacility_code = $scope.rg.village_code = "All";


    }
}




$scope.getDivisionData = function (data) {

    if (data.district_code != 'All') {
        var kwargs = {
            "query_type": "get_divisions",
            "state_code": $scope.rg.state_code,
            "zone_code": $scope.rg.zone_code,
            "district_code": $scope.rg.district_code
        }
        BlankFactory.getLocationChildrens(kwargs, $scope.django_csrf_token).then(function (response) {
            if (response.success) {

                $scope.divisionlist = response['data'];
                console.log($scope.divisionlist)

                $scope.helthblockdata = [];
                $scope.helthfacilitydata = [];
                $scope.helthsubfacilitydata = [];
                $scope.villagedata = []

                $scope.rg.division_code = "All";
                $scope.rg.block_code = "All";
                $scope.rg.facility_code = "All";
                $scope.rg.subfacility_code = "All";
                $scope.rg.village_code = "All";

            }
        })
    }
    else {

        $scope.divisionlist = [];
        $scope.helthblockdata = [];
        $scope.helthfacilitydata = [];
        $scope.helthsubfacilitydata = [];
        $scope.villagedata = [];

        $scope.rg.division_code = "All";
        $scope.rg.block_code = "All";
        $scope.rg.facility_code = "All";
        $scope.rg.subfacility_code = "All";
        $scope.rg.village_code = "All";

    }

}
$scope.getHealthBlock = function (data) {

    if (data.division_code != 'All') {
        var kwargs = {

            "query_type": "get_blocks",
            "state_code": $scope.rg.state_code,
            "zone_code": $scope.rg.zone_code,
            "district_code": $scope.rg.district_code,
            "division_code": data.division_code
        }
        BlankFactory.getLocationChildrens(kwargs, $scope.django_csrf_token).then(function (response) {
            if (response.success) {
                console.log(response);
                $scope.helthblockdata = response['data'];
                console.log($scope.helthblockdata);


                $scope.helthfacilitydata = [];
                $scope.helthsubfacilitydata = [];
                $scope.villagedata = []


                $scope.rg.block_code = "All";
                $scope.rg.facility_code = "All";
                $scope.rg.subfacility_code = "All";
                $scope.rg.village_code = "All";
            }
        })
    }
    else {

        $scope.helthblockdata = [];
        $scope.helthfacilitydata = [];
        $scope.helthsubfacilitydata = [];
        $scope.villagedata = [];

        $scope.rg.block_code = "All";
        $scope.rg.facility_code = "All";
        $scope.rg.subfacility_code = "All";
        $scope.rg.village_code = "All";


    }
}
$scope.getHealthFacility = function (data) {
    if (data.block_code != 'All') {
        var kwargs = {
            "query_type": "get_facilities",
            "state_code": $scope.rg.state_code,
            "zone_code": $scope.rg.zone_code,
            "district_code": $scope.rg.district_code,
            "division_code": $scope.rg.division_code,
            "block_code": $scope.rg.block_code
        }
        BlankFactory.getLocationChildrens(kwargs, $scope.django_csrf_token).then(function (response) {
            if (response.success) {
                // console.log(response);
                $scope.helthfacilitydata = response['data'];
                console.log($scope.helthfacilitydata);

                $scope.helthsubfacilitydata = [];
                $scope.villagedata = []


                $scope.rg.facility_code = "All";
                $scope.rg.subfacility_code = "All";
                $scope.rg.village_code = "All";
            }
        })
    }
    else {

        $scope.helthfacilitydata = [];
        $scope.helthsubfacilitydata = [];
        $scope.villagedata = []

        $scope.rg.facility_code = "All";
        $scope.rg.subfacility_code = "All";
        $scope.rg.village_code = "All";

    }
}
$scope.getHealthSubFacility = function (data) {
    if (data.facility_code != 'All') {
        var kwargs = {
            "query_type": "get_subfacilities",
            "state_code": $scope.rg.state_code,
            "zone_code": $scope.rg.zone_code,
            "district_code": $scope.rg.district_code,
            "division_code": $scope.rg.division_code,
            "block_code": $scope.rg.block_code,
            "facility_code": $scope.rg.facility_code
        }
        BlankFactory.getLocationChildrens(kwargs, $scope.django_csrf_token).then(function (response) {
            if (response.success) {
                // console.log(response);
                $scope.helthsubfacilitydata = response['data'];
                console.log($scope.helthsubfacilitydata);

                $scope.villagedata = []



                $scope.rg.subfacility_code = "All";
                $scope.rg.village_code = "All";
            }
        })
    }
    else {
        // $scope.helthblockdata=[];
        // $scope.helthfacilitydata=[];
        $scope.helthsubfacilitydata = [];
        $scope.villagedata = []
        $scope.rg.facility_code = "All";
        $scope.rg.subfacility_code = "All";
        $scope.rg.village_code = "All";
    }

}
$scope.getVillages = function (data) {
    if (data.subfacility_code != 'All') {
        var kwargs = {

            "query_type": "get_vilages",
            "state_code": $scope.rg.state_code,
            "zone_code": $scope.rg.zone_code,
            "district_code": $scope.rg.district_code,
            "division_code": $scope.rg.division_code,
            "block_code": $scope.rg.block_code,
            "facility_code": $scope.rg.facility_code,
            "subfacility_code": $scope.rg.subfacility_code
        }
        BlankFactory.getLocationChildrens(kwargs, $scope.django_csrf_token).then(function (response) {
            if (response.success) {

                $scope.villagedata = response['data'];





                $scope.rg.village_code = "All";

            }
        })
    }
    else {
        $scope.villagedata = [];
        $scope.rg.subfacility_code = "All";
        $scope.rg.village_code = "All";
    }

}


    <div class="col-6 col-md-3 col-lg-3 col-xl-3 mt-1" >
        <div class="row">
            <label class="col-md-3 col-xl-3 form-inline labelfont pl-2">Zones</label>
            <div class="col-md-9 col-xl-9">

                <select ng-model="rg.zone_code" name="zone_code" placeholder="district code" class="form-control form-control-sm" ng-change="getDistricts(rg)" >
                    <option value="All" > All</option>
                    <option ng-repeat="list in zonesList" value="{% verbatim %}{{list.zone_code}}{% endverbatim %}">{% verbatim %}{{ list.zone_name }}{% endverbatim %}</option>
                </select>
            </div>
        </div>                                                                                       
        </div >
    <div class="col-6 col-md-3 col-lg-3 col-xl-3 mt-1">
        <div class="row">
            <label class="col-md-3 col-xl-3 form-inline labelfont pl-2">District</label>
            <div class="col-md-9 col-xl-9">

                <select ng-model="rg.district_code" name="district_code" placeholder="state code" class="form-control form-control-sm" ng-change="getDivisionData(rg)" >
                    <option value="All" > All</option>
                    <option ng-repeat="list in districtlist" value="{% verbatim %}{{list.district_code}}{% endverbatim %}">{% verbatim %}{{ list.district_name }}{% endverbatim %}</option>
                </select>
            </div>
        </div>
    </div>
    <div class="col-6 col-md-3 col-lg-3 col-xl-3 mt-1">
        <div class="row">
            <label class="col-md-3 col-xl-3 form-inline labelfont pl-2">District</label>
            <div class="col-md-9 col-xl-9">

                <select ng-model="rg.division_code" name="division_code" class="form-control form-control-sm" ng-change="getHealthBlock(rg)" >
                    <option value="All" > All</option>
                    <option ng-repeat="list in divisionlist" value="{% verbatim %}{{list.division_code}}{% endverbatim %}">{% verbatim %}{{ list.division_name }}{% endverbatim %}</option>
                </select>
            </div>
        </div>
    </div>
    <div class="col-6 col-md-3 col-lg-3 col-xl-3 mt-1">
        <div class="row">
            <label class="col-md-3 col-xl-3 form-inline labelfont pl-2">Mandal</label>
            <div class="col-md-9 col-xl-9">

                <select ng-model="rg.block_code" name="block_code" placeholder="state code" class="form-control form-control-sm" ng-change="getHealthFacility(rg)" >
                    <option value="All" > All</option>
                    <option ng-repeat="list in helthblockdata" value="{% verbatim %}{{list.block_code}}{% endverbatim %}">{% verbatim %}{{ list.block_name }}{% endverbatim %}</option>
                </select>
            </div>
        </div>
    </div>
    <div class="col-6 col-md-3 col-lg-3 col-xl-3 mt-1">
        <div class="row">
            <label class="col-md-3 col-xl-3 form-inline labelfont pl-2">Facility</label>
            <div class="col-md-9 col-xl-9">

                <select ng-model="rg.facility_code" name="facility_code" placeholder="state code" class="form-control form-control-sm" ng-change="getHealthSubFacility(rg)" >
                    <option value="All" > All</option>
                    <option ng-repeat="list in helthfacilitydata" value="{% verbatim %}{{list.facility_code}}{% endverbatim %}">{% verbatim %}{{ list.facility_name }}{% endverbatim %}</option>
                </select>
            </div>
        </div>
    </div>
    <div class="col-6 col-md-3 col-lg-3 col-xl-3 mt-1">
        <div class="row">
            <label class="col-md-3 col-xl-3 form-inline labelfont pl-2">Subfacility</label>
            <div class="col-md-9 col-xl-9">

                <select ng-model="rg.subfacility_code" name="subfacility_code" placeholder="state code" class="form-control form-control-sm" ng-change="getVillages(rg)" >
                    <option value="All" > All</option>
                    <option ng-repeat="list in helthsubfacilitydata" value="{% verbatim %}{{list.subfacility_code}}{% endverbatim %}">{% verbatim %}{{ list.subfacility_name }}{% endverbatim %}</option>
                </select>
            </div>
        </div>
    </div>
    <div class="col-6 col-md-3 col-lg-3 col-xl-3 mt-1">
        <div class="row">
            <label class="col-md-3 col-xl-3 form-inline labelfont pl-2">Village</label>
            <div class="col-md-9 col-xl-9">

                <select ng-model="rg.village_code" name="village_code" placeholder="state code" class="form-control form-control-sm"  >
                    <option value="All" > All</option>
                    <option ng-repeat="list in villagedata" value="{% verbatim %}{{list.village_code}}{% endverbatim %}">{% verbatim %}{{ list.village_name }}{% endverbatim %}</option>
                </select>
            </div>
        </div>
    </div>
