"""
AMIE packets relating to users
"""

from . import Packet, PacketInvalidData


class NotifyUserModify(Packet):
    _packet_type = 'notify_account_inactivate'
    _expected_reply = ['inform_transaction_complete']
    _data_keys_required = [
        'ActionType',
        'PersonID',
    ]
    _data_keys_allowed = [
        'AcademicDegree',
        'BusinessPhoneComment',
        'BusinessPhoneExtension',
        'BusinessPhoneNumber',
        'City',
        'Country',
        'Department',
        'DnList',
        'Email',
        'Fax',
        'FirstName',
        'HomePhoneComment',
        'HomePhoneExtension',
        'HomePhoneNumber',
        'LastName',
        'MiddleName',
        'Organization',
        'OrgCode',
        'State'
    ]

    def validate_data(self, input_data):
        validated_data = super().validate_data(input_data)
        if validated_data['ActionType'] not in ['add', 'delete', 'replace']:
            error_str = "Invalid action type for notify_user_modify: {}".format(validated_data['ActionType'])
            raise PacketInvalidData(error_str)
        return validated_data


class RequestUserModify(Packet):
    _packet_type = 'request_account_inactivate'
    _expected_reply = ['inform_transaction_complete']
    _data_keys_required = [
        'ActionType',
        'PersonID',
    ]
    _data_keys_allowed = [
        'AcademicDegree',
        'BusinessPhoneComment',
        'BusinessPhoneExtension',
        'BusinessPhoneNumber',
        'CitizenshipList',
        'CitizenshipList',
        'City',
        'Country',
        'Department',
        'DnList',
        'Email',
        'Fax',
        'FirstName',
        'HomePhoneComment',
        'HomePhoneExtension',
        'HomePhoneNumber',
        'LastName',
        'MiddleName',
        'NsfStatusCode',
        'Organization',
        'OrgCode',
        'State',
        'StreetAddress',
        'StreetAddress2',
        'Title',
        'Zip',
    ]

    def validate_data(self, input_data):
        validated_data = super().validate_data(input_data)
        if validated_data['ActionType'] not in ['add', 'delete', 'replace']:
            error_str = "Invalid action type for request_user_modify: {}".format(validated_data['ActionType'])
            raise PacketInvalidData(error_str)

        return validated_data
