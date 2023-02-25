import gspread
import pandas as pd
from openpyxl import load_workbook
import re
from selenium import webdriver
import os
from selenium.webdriver.common.by import By

Zero = True
print('--------------------------------------------------')
print('Welcome')
print('--------------------------------------------------')
print("1.) Hand Cannons")
print("2.) Scout Rifles")
print("3.) Pulse Rifles")
print("4.) Auto Rifles")
print("5.) Sniper Rifles")
print("6.) Fusion Rifles")
print("7.) Bows")
print("8.) Shotguns")
print("9.) Grenade Launchers")
print("10.) Rocket Launchers")
print("11.) Linear Fusion Rifles")
print("12.) Submachine Guns")
print("13.) Sidearms")
print("14.) Machine Guns")
while Zero:

    def Main():
        Menu_2 = input('\n\npress [1] to enter an entry\nPress [2] to read the sheet\nPress [3] to find Xurs location\n-->')



        def Sub_1():
            def HC():
                print('--------------------------------------------------')
                print('Hand Cannon entry')
                print('--------------------------------------------------')
                sa = gspread.service_account(filename="destiny-2-items-78c86099653c.json")
                sh = sa.open("Destiny Weapons")
                # Sheet_title = input('Enter Day\n')

                Name_1 = input('Name\n-->')
                IH_1 = input('Item Hash\n-->')
                try:
                    Impact_1 = int (input('Impact\n-->'))
                except:
                    pass
                try:
                    Range_1 = int (input('Range\n-->'))
                except:
                    pass
                try:
                    Stabil_1 = int (input('Stability\n-->'))
                except:
                    pass
                try:
                    Handl_1 = int (input('Handling\n-->'))
                except:
                    pass
                Rld_1 = input('Reload Speed\n-->')
                Rpm_1 = input('Rounds per minute\n-->')
                Mag_1 = input('Magazine\n-->')
                try:
                    Avg_H1 = Impact_1 + Range_1 + Stabil_1 + Handl_1
                except:
                    pass

                try:
                    Avg_H2 = Avg_H1/4
                except:
                    pass
                print('--------------------------------------------------')
                print('Average')
                try:
                    print(Avg_H2)
                except:
                    pass

                wks = sh.worksheet('Hand Cannons')
                try:
                    df = pd.DataFrame({'Name': [Name_1], 'Item Hash': [IH_1], 'Impact': [Impact_1], 'Range': [Range_1],
                                    'Stability': [Stabil_1], 'Handling': [Handl_1],
                                    'Reload Speed': [Rld_1], 'Rounds per minute': [Rpm_1], 'Magazine': [Mag_1], 'Average': [Avg_H2]})
                except:
                    pass
                try:
                    df_values = df.values.tolist()
                except:
                    pass
                try:
                    sh.values_append('Hand Cannons', {'valueInputOption': 'RAW'}, {'values': df_values})
                except:
                    pass

            def SR():
                print('--------------------------------------------------')
                print('Scout Rifles entry')
                print('--------------------------------------------------')
                sa = gspread.service_account(filename="destiny-2-items-78c86099653c.json")
                sh = sa.open("Destiny Weapons")
                # Sheet_title = input('Enter Day\n')

                Name_2 = input('Name\n-->')
                IH_2 = (input('Item Hash\n-->'))
                try:
                    Impact_2 = int (input('Impact\n-->'))
                except:
                    pass
                try:
                    Range_2 = int (input('Range\n-->'))
                except:
                    pass
                try:
                    Stabil_2 = int (input('Stability\n-->'))
                except:
                    pass
                try:
                    Handl_2 = int (input('Handling\n-->'))
                except:
                    pass

                Rld_2 = input('Reload Speed\n-->')
                Rpm_2 = input('Rounds per minute\n-->')
                Mag_2 = input('Magazine\n-->')
                try:
                    Avg_SR1 = Impact_2 + Range_2 + Stabil_2 + Handl_2
                except:
                    pass
                try:
                    Avg_SR2 = Avg_SR1/4
                except:
                    pass
                print('--------------------------------------------------')
                print('Average')


                try:
                    print(Avg_SR2)
                except:
                    pass


                wks = sh.worksheet('Scout Rifles')
                try:
                    df = pd.DataFrame({'Name': [Name_2], 'Item Hash': [IH_2], 'Impact': [Impact_2], 'Range': [Range_2],
                                   'Stability': [Stabil_2], 'Handling': [Handl_2],
                                   'Reload Speed': [Rld_2], 'Rounds per minute': [Rpm_2], 'Magazine': [Mag_2], 'Average': [Avg_SR2]})
                except:
                    pass
                try:
                    df_values = df.values.tolist()
                except:
                    pass


                try:
                    sh.values_append('Scout Rifles', {'valueInputOption': 'RAW'}, {'values': df_values})
                except:
                    pass

            def PR():
                print('--------------------------------------------------')
                print('Pulse Rifles entry')
                print('--------------------------------------------------')
                sa = gspread.service_account(filename="destiny-2-items-78c86099653c.json")
                sh = sa.open("Destiny Weapons")
                # Sheet_title = input('Enter Day\n')

                Name_3 = input('Name\n-->')
                IH_3 = (input('Item Hash\n-->'))
                try:
                    Impact_3 = int (input('Impact\n-->'))
                except:
                    pass
                try:
                    Range_3 = int (input('Range\n-->'))
                except:
                    pass
                try:
                    Stabil_3 = int (input('Stability\n-->'))
                except:
                    pass
                try:
                    Handl_3 = int (input('Handling\n-->'))
                except:
                    pass

                Rld_3 = input('Reload Speed\n-->')
                Rpm_3 = input('Rounds per minute\n-->')
                Mag_3 = input('Magazine\n-->')
                try:
                    Avg_PR1 = Impact_3 + Range_3 + Stabil_3 + Handl_3
                except:
                    pass
                try:
                    Avg_PR2 = Avg_PR1/4
                except:
                    pass
                print('--------------------------------------------------')
                print('Average')


                try:
                    print(Avg_PR2)
                except:
                    pass


                wks = sh.worksheet('Pulse Rifles')
                try:
                    df = pd.DataFrame({'Name': [Name_3], 'Item Hash': [IH_3], 'Impact': [Impact_3], 'Range': [Range_3],
                                   'Stability': [Stabil_3], 'Handling': [Handl_3],
                                   'Reload Speed': [Rld_3], 'Rounds per minute': [Rpm_3], 'Magazine': [Mag_3], 'Average': [Avg_PR2]})
                except:
                    pass
                try:
                    df_values = df.values.tolist()
                except:
                    pass


                try:
                    sh.values_append('Pulse Rifles', {'valueInputOption': 'RAW'}, {'values': df_values})
                except:
                    pass


            def AR():
                print('--------------------------------------------------')
                print('Auto Rifles entry')
                print('--------------------------------------------------')
                sa = gspread.service_account(filename="destiny-2-items-78c86099653c.json")
                sh = sa.open("Destiny Weapons")
                # Sheet_title = input('Enter Day\n')

                Name_4 = input('Name\n-->')
                IH_4 = (input('Item Hash\n-->'))
                try:
                    Impact_4 = int (input('Impact\n-->'))
                except:
                    pass
                try:
                    Range_4 = int (input('Range\n-->'))
                except:
                    pass
                try:
                    Stabil_4 = int (input('Stability\n-->'))
                except:
                    pass
                try:
                    Handl_4 = int (input('Handling\n-->'))
                except:
                    pass

                Rld_4 = input('Reload Speed\n-->')
                Rpm_4 = input('Rounds per minute\n-->')
                Mag_4 = input('Magazine\n-->')
                try:
                    Avg_AR1 = Impact_4 + Range_4 + Stabil_4 + Handl_4
                except:
                    pass
                try:
                    Avg_AR2 = Avg_AR1/4
                except:
                    pass
                print('--------------------------------------------------')
                print('Average')


                try:
                    print(Avg_AR2)
                except:
                    pass


                wks = sh.worksheet('Auto Rifles')
                try:
                    df = pd.DataFrame({'Name': [Name_4], 'Item Hash': [IH_4], 'Impact': [Impact_4], 'Range': [Range_4],
                                   'Stability': [Stabil_4], 'Handling': [Handl_4],
                                   'Reload Speed': [Rld_4], 'Rounds per minute': [Rpm_4], 'Magazine': [Mag_4], 'Average': [Avg_AR2]})
                except:
                    pass
                try:
                    df_values = df.values.tolist()
                except:
                    pass


                try:
                    sh.values_append('Auto Rifles', {'valueInputOption': 'RAW'}, {'values': df_values})
                except:
                    pass


            def SNR():
                print('--------------------------------------------------')
                print('Sniper Rifles entry')
                print('--------------------------------------------------')
                sa = gspread.service_account(filename="destiny-2-items-78c86099653c.json")
                sh = sa.open("Destiny Weapons")
                # Sheet_title = input('Enter Day\n')

                Name_5 = input('Name\n-->')
                IH_5 = (input('Item Hash\n-->'))
                try:
                    Impact_5 = int (input('Impact\n-->'))
                except:
                    pass
                try:
                    Range_5 = int (input('Range\n-->'))
                except:
                    pass
                try:
                    Stabil_5 = int (input('Stability\n-->'))
                except:
                    pass
                try:
                    Handl_5 = int (input('Handling\n-->'))
                except:
                    pass

                Rld_5 = input('Reload Speed\n-->')
                Rpm_5 = input('Rounds per minute\n-->')
                Mag_5 = input('Magazine\n-->')
                try:
                    Avg_SNR1 = Impact_5 + Range_5 + Stabil_5 + Handl_5
                except:
                    pass
                try:
                    Avg_SNR2 = Avg_SNR1/4
                except:
                    pass
                print('--------------------------------------------------')
                print('Average')


                try:
                    print(Avg_SNR2)
                except:
                    pass


                wks = sh.worksheet('Sniper Rifles')
                try:
                    df = pd.DataFrame({'Name': [Name_5], 'Item Hash': [IH_5], 'Impact': [Impact_5], 'Range': [Range_5],
                                   'Stability': [Stabil_5], 'Handling': [Handl_5],
                                   'Reload Speed': [Rld_5], 'Rounds per minute': [Rpm_5], 'Magazine': [Mag_5], 'Average': [Avg_SNR2]})
                except:
                    pass
                try:
                    df_values = df.values.tolist()
                except:
                    pass


                try:
                    sh.values_append('Sniper Rifles', {'valueInputOption': 'RAW'}, {'values': df_values})
                except:
                    pass

            def FR():
                print('--------------------------------------------------')
                print('Fusion Rifles entry')
                print('--------------------------------------------------')
                sa = gspread.service_account(filename="destiny-2-items-78c86099653c.json")
                sh = sa.open("Destiny Weapons")
                # Sheet_title = input('Enter Day\n')

                Name_6 = input('Name\n-->')
                IH_6 = (input('Item Hash\n-->'))
                try:
                    Impact_6 = int (input('Impact\n-->'))
                except:
                    pass
                try:
                    Range_6 = int (input('Range\n-->'))
                except:
                    pass
                try:
                    Stabil_6 = int (input('Stability\n-->'))
                except:
                    pass
                try:
                    Handl_6 = int (input('Handling\n-->'))
                except:
                    pass

                Rld_6 = input('Reload Speed\n-->')
                Rpm_6 = input('Charge Time\n-->')
                Mag_6 = input('Magazine\n-->')
                try:
                    Avg_FR1 = Impact_6 + Range_6 + Stabil_6 + Handl_6
                except:
                    pass
                try:
                    Avg_FR2 = Avg_FR1/4
                except:
                    pass
                print('--------------------------------------------------')
                print('Average')


                try:
                    print(Avg_FR2)
                except:
                    pass


                wks = sh.worksheet('Fusion Rifles')
                try:
                    df = pd.DataFrame({'Name': [Name_6], 'Item Hash': [IH_6], 'Impact': [Impact_6], 'Range': [Range_6],
                                   'Stability': [Stabil_6], 'Handling': [Handl_6],
                                   'Reload Speed': [Rld_6], 'Charge Time': [Rpm_6], 'Magazine': [Mag_6], 'Average': [Avg_FR2]})
                except:
                    pass
                try:
                    df_values = df.values.tolist()
                except:
                    pass


                try:
                    sh.values_append('Fusion Rifles', {'valueInputOption': 'RAW'}, {'values': df_values})
                except:
                    pass


            def BOW():
                print('--------------------------------------------------')
                print('Bows entry')
                print('--------------------------------------------------')
                sa = gspread.service_account(filename="destiny-2-items-78c86099653c.json")
                sh = sa.open("Destiny Weapons")
                # Sheet_title = input('Enter Day\n')

                Name_7 = input('Name\n-->')
                IH_7 = (input('Item Hash\n-->'))
                try:
                    Impact_7 = int (input('Impact\n-->'))
                except:
                    pass
                try:
                    Range_7 = int (input('Range\n-->'))
                except:
                    pass
                try:
                    Stabil_7 = int (input('Stability\n-->'))
                except:
                    pass
                try:
                    Handl_7 = int (input('Handling\n-->'))
                except:
                    pass

                Rld_7 = input('Reload Speed\n-->')
                Rpm_7 = input('Draw Time\n-->')
                Mag_7 = input('Magazine\n-->')
                try:
                    Avg_BO1 = Impact_7 + Range_7 + Stabil_7 + Handl_7
                except:
                    pass
                try:
                    Avg_BO2 = Avg_BO1/4
                except:
                    pass
                print('--------------------------------------------------')
                print('Average')


                try:
                    print(Avg_BO2)
                except:
                    pass


                wks = sh.worksheet('Bows')
                try:
                    df = pd.DataFrame({'Name': [Name_7], 'Item Hash': [IH_7], 'Impact': [Impact_7], 'Range': [Range_7],
                                   'Stability': [Stabil_7], 'Handling': [Handl_7],
                                   'Reload Speed': [Rld_7], 'Charge Time': [Rpm_7], 'Draw Time': [Mag_7], 'Average': [Avg_BO2]})
                except:
                    pass
                try:
                    df_values = df.values.tolist()
                except:
                    pass


                try:
                    sh.values_append('Bows', {'valueInputOption': 'RAW'}, {'values': df_values})
                except:
                    pass


            def SHO():
                print('--------------------------------------------------')
                print('Shotguns entry')
                print('--------------------------------------------------')
                sa = gspread.service_account(filename="destiny-2-items-78c86099653c.json")
                sh = sa.open("Destiny Weapons")
                # Sheet_title = input('Enter Day\n')

                Name_8 = input('Name\n-->')
                IH_8 = (input('Item Hash\n-->'))
                try:
                    Impact_8 = int (input('Impact\n-->'))
                except:
                    pass
                try:
                    Range_8 = int (input('Range\n-->'))
                except:
                    pass
                try:
                    Stabil_8 = int (input('Stability\n-->'))
                except:
                    pass
                try:
                    Handl_8 = int (input('Handling\n-->'))
                except:
                    pass

                Rld_8 = input('Reload Speed\n-->')
                Rpm_8 = input('Rounds per minute\n-->')
                Mag_8 = input('Magazine\n-->')
                try:
                    Avg_SHO1 = Impact_8 + Range_8 + Stabil_8 + Handl_8
                except:
                    pass
                try:
                    Avg_SHO2 = Avg_SHO1/4
                except:
                    pass
                print('--------------------------------------------------')
                print('Average')


                try:
                    print(Avg_SHO2)
                except:
                    pass


                wks = sh.worksheet('Shotguns')
                try:
                    df = pd.DataFrame({'Name': [Name_8], 'Item Hash': [IH_8], 'Impact': [Impact_8], 'Range': [Range_8],
                                   'Stability': [Stabil_8], 'Handling': [Handl_8],
                                   'Reload Speed': [Rld_8], 'Rounds per minute': [Rpm_8], 'Magazine': [Mag_8], 'Average': [Avg_SHO2]})
                except:
                    pass
                try:
                    df_values = df.values.tolist()
                except:
                    pass


                try:
                    sh.values_append('Shotguns', {'valueInputOption': 'RAW'}, {'values': df_values})
                except:
                    pass

            def GL():
                print('--------------------------------------------------')
                print('Grenade Launchers entry')
                print('--------------------------------------------------')
                sa = gspread.service_account(filename="destiny-2-items-78c86099653c.json")
                sh = sa.open("Destiny Weapons")
                # Sheet_title = input('Enter Day\n')

                Name_9 = input('Name\n-->')
                IH_9 = (input('Item Hash\n-->'))
                try:
                    Impact_9 = int (input('Blast Radius\n-->'))
                except:
                    pass
                try:
                    Range_9 = int (input('Velocity\n-->'))
                except:
                    pass
                try:
                    Stabil_9 = int (input('Stability\n-->'))
                except:
                    pass
                try:
                    Handl_9 = int (input('Handling\n-->'))
                except:
                    pass

                Rld_9 = input('Reload Speed\n-->')
                Rpm_9 = input('Rounds per minute\n-->')
                Mag_9 = input('Magazine\n-->')
                try:
                    Avg_GL1 = Impact_9 + Range_9 + Stabil_9 + Handl_9
                except:
                    pass
                try:
                    Avg_GL2 = Avg_GL1/4
                except:
                    pass
                print('--------------------------------------------------')
                print('Average')


                try:
                    print(Avg_GL2)
                except:
                    pass


                wks = sh.worksheet('Grenade Launchers')
                try:
                    df = pd.DataFrame({'Name': [Name_9], 'Item Hash': [IH_9], 'Blast Radius': [Impact_9], 'Velocity': [Range_9],
                                   'Stability': [Stabil_9], 'Handling': [Handl_9],
                                   'Reload Speed': [Rld_9], 'Rounds per minute': [Rpm_9], 'Magazine': [Mag_9], 'Average': [Avg_GL2]})
                except:
                    pass
                try:
                    df_values = df.values.tolist()
                except:
                    pass


                try:
                    sh.values_append('Grenade Launchers', {'valueInputOption': 'RAW'}, {'values': df_values})
                except:
                    pass


            def RL():
                print('--------------------------------------------------')
                print('Rocket Launchers entry')
                print('--------------------------------------------------')
                sa = gspread.service_account(filename="destiny-2-items-78c86099653c.json")
                sh = sa.open("Destiny Weapons")
                # Sheet_title = input('Enter Day\n')

                Name_10 = input('Name\n-->')
                IH_10 = (input('Item Hash\n-->'))
                try:
                    Impact_10 = int (input('Blast Radius\n-->'))
                except:
                    pass
                try:
                    Range_10 = int (input('Velocity\n-->'))
                except:
                    pass
                try:
                    Stabil_10 = int (input('Stability\n-->'))
                except:
                    pass
                try:
                    Handl_10 = int (input('Handling\n-->'))
                except:
                    pass

                Rld_10 = input('Reload Speed\n-->')
                Rpm_10 = input('Rounds per minute\n-->')
                Mag_10 = input('Magazine\n-->')
                try:
                    Avg_RL1 = Impact_10 + Range_10 + Stabil_10 + Handl_10
                except:
                    pass
                try:
                    Avg_RL2 = Avg_RL1/4
                except:
                    pass
                print('--------------------------------------------------')
                print('Average')


                try:
                    print(Avg_RL2)
                except:
                    pass


                wks = sh.worksheet('Rocket Launchers')
                try:
                    df = pd.DataFrame({'Name': [Name_10], 'Item Hash': [IH_10], 'Blast Radius': [Impact_10], 'Velocity': [Range_10],
                                   'Stability': [Stabil_10], 'Handling': [Handl_10],
                                   'Reload Speed': [Rld_10], 'Rounds per minute': [Rpm_10], 'Magazine': [Mag_10], 'Average': [Avg_RL2]})
                except:
                    pass
                try:
                    df_values = df.values.tolist()
                except:
                    pass


                try:
                    sh.values_append('Rocket Launchers', {'valueInputOption': 'RAW'}, {'values': df_values})
                except:
                    pass

            def LFR():
                print('--------------------------------------------------')
                print('Linear Fusion Rifles entry')
                print('--------------------------------------------------')
                sa = gspread.service_account(filename="destiny-2-items-78c86099653c.json")
                sh = sa.open("Destiny Weapons")
                # Sheet_title = input('Enter Day\n')

                Name_11 = input('Name\n-->')
                IH_11 = (input('Item Hash\n-->'))
                try:
                    Impact_11 = int(input('Impact\n-->'))
                except:
                    pass
                try:
                    Range_11 = int(input('Range\n-->'))
                except:
                    pass
                try:
                    Stabil_11 = int(input('Stability\n-->'))
                except:
                    pass
                try:
                    Handl_11 = int(input('Handling\n-->'))
                except:
                    pass

                Rld_11 = input('Reload Speed\n-->')
                Rpm_11 = input('Charge Time\n-->')
                Mag_11 = input('Magazine\n-->')
                try:
                    Avg_LFR1 = Impact_11 + Range_11 + Stabil_11 + Handl_11
                except:
                    pass
                try:
                    Avg_LFR2 = Avg_LFR1 / 4
                except:
                    pass
                print('--------------------------------------------------')
                print('Average')

                try:
                    print(Avg_LFR2)
                except:
                    pass

                wks = sh.worksheet('Linear Fusion Rifles')
                try:
                    df = pd.DataFrame(
                        {'Name': [Name_11], 'Item Hash': [IH_11], 'Impact': [Impact_11], 'Range': [Range_11],
                         'Stability': [Stabil_11], 'Handling': [Handl_11],
                         'Reload Speed': [Rld_11], 'Charge Time': [Rpm_11], 'Magazine': [Mag_11],
                         'Average': [Avg_LFR2]})
                except:
                    pass
                try:
                    df_values = df.values.tolist()
                except:
                    pass

                try:
                    sh.values_append('Linear Fusion Rifles', {'valueInputOption': 'RAW'}, {'values': df_values})
                except:
                    pass


            def SMG():
                print('--------------------------------------------------')
                print('Submachine Guns entry')
                print('--------------------------------------------------')
                sa = gspread.service_account(filename="destiny-2-items-78c86099653c.json")
                sh = sa.open("Destiny Weapons")
                # Sheet_title = input('Enter Day\n')

                Name_12 = input('Name\n-->')
                IH_12 = (input('Item Hash\n-->'))
                try:
                    Impact_12 = int (input('Impact\n-->'))
                except:
                    pass
                try:
                    Range_12 = int (input('Range\n-->'))
                except:
                    pass
                try:
                    Stabil_12 = int (input('Stability\n-->'))
                except:
                    pass
                try:
                    Handl_12 = int (input('Handling\n-->'))
                except:
                    pass

                Rld_12 = input('Reload Speed\n-->')
                Rpm_12 = input('Rounds per minute\n-->')
                Mag_12 = input('Magazine\n-->')
                try:
                    Avg_SMG1 = Impact_12 + Range_12 + Stabil_12 + Handl_12
                except:
                    pass
                try:
                    Avg_SMG2 = Avg_SMG1/4
                except:
                    pass
                print('--------------------------------------------------')
                print('Average')


                try:
                    print(Avg_SMG2)
                except:
                    pass


                wks = sh.worksheet('Submachine Guns')
                try:
                    df = pd.DataFrame({'Name': [Name_12], 'Item Hash': [IH_12], 'Impact': [Impact_12], 'Range': [Range_12],
                                   'Stability': [Stabil_12], 'Handling': [Handl_12],
                                   'Reload Speed': [Rld_12], 'Rounds per minute': [Rpm_12], 'Magazine': [Mag_12], 'Average': [Avg_SMG2]})
                except:
                    pass
                try:
                    df_values = df.values.tolist()
                except:
                    pass


                try:
                    sh.values_append('Submachine Guns', {'valueInputOption': 'RAW'}, {'values': df_values})
                except:
                    pass


            def SAR():
                print('--------------------------------------------------')
                print('Sidearms entry')
                print('--------------------------------------------------')
                sa = gspread.service_account(filename="destiny-2-items-78c86099653c.json")
                sh = sa.open("Destiny Weapons")
                # Sheet_title = input('Enter Day\n')

                Name_13 = input('Name\n-->')
                IH_13 = (input('Item Hash\n-->'))
                try:
                    Impact_13 = int (input('Impact\n-->'))
                except:
                    pass
                try:
                    Range_13 = int (input('Range\n-->'))
                except:
                    pass
                try:
                    Stabil_13 = int (input('Stability\n-->'))
                except:
                    pass
                try:
                    Handl_13 = int (input('Handling\n-->'))
                except:
                    pass

                Rld_13 = input('Reload Speed\n-->')
                Rpm_13 = input('Rounds per minute\n-->')
                Mag_13 = input('Magazine\n-->')
                try:
                    Avg_SAR1 = Impact_13 + Range_13 + Stabil_13 + Handl_13
                except:
                    pass
                try:
                    Avg_SAR2 = Avg_SAR1/4
                except:
                    pass
                print('--------------------------------------------------')
                print('Average')


                try:
                    print(Avg_SAR2)
                except:
                    pass


                wks = sh.worksheet('Sidearms')
                try:
                    df = pd.DataFrame({'Name': [Name_13], 'Item Hash': [IH_13], 'Impact': [Impact_13], 'Range': [Range_13],
                                   'Stability': [Stabil_13], 'Handling': [Handl_13],
                                   'Reload Speed': [Rld_13], 'Rounds per minute': [Rpm_13], 'Magazine': [Mag_13], 'Average': [Avg_SAR2]})
                except:
                    pass
                try:
                    df_values = df.values.tolist()
                except:
                    pass


                try:
                    sh.values_append('Sidearms', {'valueInputOption': 'RAW'}, {'values': df_values})
                except:
                    pass


            def MG():
                print('--------------------------------------------------')
                print('Machine Guns entry')
                print('--------------------------------------------------')
                sa = gspread.service_account(filename="destiny-2-items-78c86099653c.json")
                sh = sa.open("Destiny Weapons")
                # Sheet_title = input('Enter Day\n')

                Name_14 = input('Name\n-->')
                IH_14 = (input('Item Hash\n-->'))
                try:
                    Impact_14 = int (input('Impact\n-->'))
                except:
                    pass
                try:
                    Range_14 = int (input('Range\n-->'))
                except:
                    pass
                try:
                    Stabil_14 = int (input('Stability\n-->'))
                except:
                    pass
                try:
                    Handl_14 = int (input('Handling\n-->'))
                except:
                    pass

                Rld_14 = input('Reload Speed\n-->')
                Rpm_14 = input('Rounds per minute\n-->')
                Mag_14 = input('Magazine\n-->')
                try:
                    Avg_MG1 = Impact_14 + Range_14 + Stabil_14 + Handl_14
                except:
                    pass
                try:
                    Avg_MG2 = Avg_MG1/4
                except:
                    pass
                print('--------------------------------------------------')
                print('Average')


                try:
                    print(Avg_MG2)
                except:
                    pass


                wks = sh.worksheet('Machine Guns')
                try:
                    df = pd.DataFrame({'Name': [Name_14], 'Item Hash': [IH_14], 'Impact': [Impact_14], 'Range': [Range_14],
                                   'Stability': [Stabil_14], 'Handling': [Handl_14],
                                   'Reload Speed': [Rld_14], 'Rounds per minute': [Rpm_14], 'Magazine': [Mag_14], 'Average': [Avg_MG2]})
                except:
                    pass
                try:
                    df_values = df.values.tolist()
                except:
                    pass


                try:
                    sh.values_append('Machine Guns', {'valueInputOption': 'RAW'}, {'values': df_values})
                except:
                    pass


            print('--------------------------------------------------')
            print("1.) Hand Cannons")
            print("2.) Scout Rifles")
            print("3.) Pulse Rifles")
            print("4.) Auto Rifles")
            print("5.) Sniper Rifles")
            print("6.) Fusion Rifles")
            print("7.) Bows")
            print("8.) Shotguns")
            print("9.) Grenade Launchers")
            print("10.) Rocket Launchers")
            print("11.) Linear Fusion Rifles")
            print("12.) Submachine Guns")
            print("13.) Sidearms")
            print("14.) Machine Guns")

            gun_st = input("\nPress 1 - 10 to enter stats for that Gun\n-->")
            print('')




            if gun_st == "1":
                HC()

            if gun_st == "2":
                SR()

            if gun_st == "3":
                PR()

            if gun_st == "4":
                AR()

            if gun_st == "5":
                SNR()

            if gun_st == "6":
                FR()

            if gun_st == "7":
                BOW()

            if gun_st == "8":
                SHO()

            if gun_st == "9":
                GL()

            if gun_st == "10":
                RL()

            if gun_st == "11":
                LFR()

            if gun_st == "12":
                SMG()

            if gun_st == "13":
                SAR()

            if gun_st == "14":
                MG()




        def Sub_2():
            # read
            aa = gspread.service_account(filename="destiny-2-items-78c86099653c.json")
            shee = aa.open("Destiny Weapons")
            try:
                Sheet_title = input('Enter Sheet title\n-->')
            except:
                pass
            try:
                wks_2 = shee.worksheet(Sheet_title)
            except:
                pass
            #print(wks_2.get_all_records())
            try:
                for i in wks_2.get_all_records():
                    print(i)
            except:
                pass

        def Sub_3():
            os.environ['PATH'] += r"C:\Program Files (x86)\chromedriver.exe"

            PATH = "C:\Program Files (x86)\chromedriver.exe"
            driver = webdriver.Chrome(PATH)
            driver.get("https://whereisxur.com/")
            Xur_is = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/article/div/div/div/div[2]/div[1]/div[1]/div[2]/div/h4")
            Xur_what = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/article/div/div/div/div[4]/div[1]/div/div/div/h2")
            Xur_weapon = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/article/div/div/div/div[4]/div[2]/div[1]/div[2]/div/div/h4/span")
            Xur_weapon2 = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/article/div/div/div/div[4]/div[2]/div[1]/div[2]/div/div/div/p")
            Xur_Hunter = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/article/div/div/div/div[4]/div[2]/div[2]/div[2]/div/div/h4/span")
            Xur_Hunter2 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/article/div/div/div/div[4]/div[2]/div[2]/div[2]/div/div/div/p")

            print(Xur_is)
            print(Xur_what)
            print(Xur_weapon)
            print(Xur_weapon2)
            print(Xur_Hunter)
            print(Xur_Hunter2)


        if Menu_2 == '1':
            Sub_1()

        elif Menu_2 == '2':
            Sub_2()

        elif Menu_2 == '3':
            Sub_3()

    print('--------------------------------------------------')

    ext = input('Press y to continue or x to exit\n-->')

    if ext == 'y':
        Zero = True
        Main()
    elif ext == 'x':
        Zero = False
    else:
        Zero = False


# any input is string
#number = input("Please guess what number I'm thinking of. HINT: it's between 1 and 30: ")
#try:                      # if possible, try to convert the input into integer
 #   number = int(number)
#except:                   # if the input couldn't be converted into integer, then do nothing
 #   pass
#print(type(number))       # see the input type after processing
