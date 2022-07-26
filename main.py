# -*- encoding: utf-8 -*-
import gettext
_ = gettext.gettext
# l10n = gettext.translation("zh_CN", localedir="locale", languages=["zh_CN"])
# l10n.install()
# _ = l10n.gettext


print(_("Edit"))
print(_("Cancel"))
print(_("Confirm"))


'''
xgettext -k_ -o locale/zh_CN/LC_MESSAGES_1/zh_CN.po main.py

msgfmt -o locale/zh_CN/LC_MESSAGES_1/zh_CN.mo locale/zh_CN/LC_MESSAGES_1/zh_CN.po

'''