
class TableFoBankCashBal:
    def __init__(self, family_id):
        self.TableName =  "FoBankCashBal_"  + family_id
        self.TableType = "FoBankCashBal"
        self.KeyAttributes = [
            {
              "AttributeName": "AC_NBR",
                "KeyType": "HASH"
            },
            {
              "AttributeName": "CURR",
                "KeyType": "RANGE"
            }]
        self.Tags = [
            {
                "Key": "table",
                'Value': family_id
            }
        ]

        self.KeyAttributeDefinitions = [
            {
                "AttributeName": "AC_NBR",
                "AttributeType": "S"
            },
            {
                "AttributeName": "CURR",
                "AttributeType": "S"
            }
        ]
        self.NonKeyAttributes =  [
            {
                "AttributeName": "FAMILY_ID",
                "AttributeType": "S"
            },

            {
              "AttributeName": "LEDGER DATE",
              "AttributeType": "S"
            },
            {
              "AttributeName": "BANK NAME",
              "AttributeType": "S"
            },
            {
              "AttributeName": "BANK ACCOUNT LONG NAME",
              "AttributeType": "S"
            },
            {
              "AttributeName": "BANK AC SHORT NAME",
              "AttributeType": "S"
            },
            {
              "AttributeName": "AC_TYPE",
              "AttributeType": "S"
            },
            {
              "AttributeName": "AVAIL_BAL",
              "AttributeType": "N"
            },
            {
              "AttributeName": "RBC_EQV_AVAIL_BAL",
              "AttributeType": "N"
            }
      ]



class TableFoCashTrans:
    def __init__(self, family_id):
        self.TableName = "FoCashTrans_" + family_id
        self.TableType = "FoCashTrans"
        self.Tags = [
            {
                "Key": "table",
                'Value': family_id
            }
        ]
        self.KeyAttributes = [
            {
                "AttributeName": "AC_NBR",
                "KeyType": "HASH"
            },
            {
                "AttributeName": "CURR",
                "KeyType": "RANGE"
            }
        ]

        self.KeyAttributeDefinitions = [
            {
                "AttributeName": "AC_NBR",
                "AttributeType": "S"
            },
            {
                "AttributeName": "CURR",
                "AttributeType": "S"
            }
        ]
        self.NonKeyAttributes =  [

            {
                "AttributeName": "FAMILY_ID",
                "AttributeType": "S"
            },

            {
                "AttributeName": "LEDGER DATE",
                "AttributeType": "S"
            },
            {
                "AttributeName": "Bank Short Name",
                "AttributeType": "S"
            },
            {
                "AttributeName": "DESCRIPTION",
                "AttributeType": "S"
            },
            {
                "AttributeName": "TRAN_AMT",
                "AttributeType": "N"
            },
            {
                "AttributeName": "HKD EQV",
                "AttributeType": "N"
            },
      ]



class TableFoInvestSummary:
    def __init__(self, family_id):
        self.TableName = "FoInvestSummary_" + family_id
        self.TableType = "FoInvestSummary"
        self.Tags = [
            {
                "Key": "table",
                'Value': family_id
            }
        ]
        self.KeyAttributes = [
            {
                "AttributeName": "FAMILY_ID",
                "KeyType": "HASH"
            },
            {
                "AttributeName": "SEQ_NO",
                "KeyType": "RANGE"
            }
        ]

        self.KeyAttributeDefinitions =  [
            {
                "AttributeName": "FAMILY_ID",
                "AttributeType": "S"
            },
            {
                "AttributeName": "SEQ_NO",
                "AttributeType": "S"
            }]

        self.NonKeyAttributes = [
            {
                "AttributeName": "INVEST_CLASS",
                "AttributeType": "S"
            },
            {
                "AttributeName": "INVEST_SUB_TYPE",
                "AttributeType": "S"
            },
            {
                "AttributeName": "INSTRUMENT_CODE",
                "AttributeType": "S"
            },
            {
                "AttributeName": "INVEST_CURR",
                "AttributeType": "S"
            },
            {
                "AttributeName": "THIS PERIOD VALUE",
                "AttributeType": "N"
            },
            {
                "AttributeName": "COST BASIS",
                "AttributeType": "N"
            },
            {
                "AttributeName": "UNREALISED GAIN LOSS",
                "AttributeType": "N"
            },
            {
                "AttributeName": "ESTIMATE ANNUAL INCOME",
                "AttributeType": "N"
            },
            {
                "AttributeName": "HKD EQV THIS PERIOD",
                "AttributeType": "S"
            },
            {
                "AttributeName": "CUSTODIAN",
                "AttributeType": "S"
            },
            {
                "AttributeName": "LEDGER DATE",
                "AttributeType": "S"
            }

      ]

'''
There is a table definition factory where you can get table definition according to the table TYPE you provided,
however table type should be in scope we supported. 
'''
class tableFactory:
    def __init__(self, ):
        self.TableType = {'FoInvestSummary': TableFoInvestSummary,
                          'FoCashTrans': TableFoCashTrans,
                          'FoBankCashBal': TableFoBankCashBal,}

    def tableDefinition(self, table_type, family_id):
        table_type_existed = table_type in self.TableType.keys()
        if table_type_existed:
            table_definition_class = self.TableType[table_type]
            table_definition = table_definition_class(family_id)
            return {
                table_definition.TableName: table_definition,
            }
        else:
            return None

