import PySimpleGUI as sg
import time
import gettext
import factory


_, img = factory.valid_code()
domain = "zh_CN"
_ = gettext.gettext
if domain == "zh_CN":
    l10n = gettext.translation("zh_CN", localedir="../locale/predict_captcha", languages=["zh_CN"])
    l10n.install()
    _ = l10n.gettext

sg.theme('DarkAmber')

layout = [
    [sg.Text("")],
    [sg.Text(_("Captcha") + ":", size=(6, 1)), sg.Image(source=img),
     sg.InputText(size=(6, 1)), sg.Button(_('Predict'), size=(7, 1))],
    [sg.ProgressBar(100, orientation="h", size=(39, 20), key='progressbar')],
    [sg.Text("")],
]

window = sg.Window(_('Predict Captcha'), layout)
progress_bar = window['progressbar']


def mock_bar(start, end, t):
    for _i in range(start, end + 1):
        progress_bar.update(_i)
        time.sleep(t)


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break
    if event == _('Predict'):
        mock_bar(1, 60, 0.01)
        mock_bar(60, 70, 0.07)
        mock_bar(71, 80, 0.05)
        time.sleep(1)
        mock_bar(81, 100, 0.005)
        time.sleep(0.5)
        sg.popup(_("Captcha is ") + values[1] + "！")

window.close()
