=============================
Sphinx 1.2 preview 2013/2/23
=============================

おまえ、誰よ
=============
.. figure:: face.png

* `http://清水川.jp/ <http://清水川.jp/>`_
  `@shimizukawa <http://twitter.com/shimizukawa>`_
* Sphinxの活動:
   * Sphinxメンテナー、Sphinx-users.jp会長
* その他の活動:
   * Zope/Plone系, pyspa系, XP系
* 言語:
   * C++/C/8086 -> Python/Rails

.. figure:: sphinxusers.jpg


.. s6:: effect slide

.. s6:: styles

    'ul': {fontSize:'65%'},
    'div[0]': {width:'15%', position:'absolute', top:0},
    'div[1]': {width:'60%', float:'right'},
    'ul/li': {display: 'none'},

.. s6:: actions

    ['ul/li[0]', 'fade in', '0.3'],
    ['ul/li[1]', 'fade in', '0.3'],
    ['ul/li[2]', 'fade in', '0.3'],
    ['ul/li[3]', 'fade in', '0.3'],


Sphinx 1.2 のリリース時期
===========================

.. figure:: sphinx-1.2-release-day.png

.. figure:: sphinx-1.2-release-day2.png

* そろそろ旧正月も明けたよね！

.. s6:: effect slide

.. s6:: styles

    'div[0]': {width:'90%', position:'absolute', top:'40%', display: 'none'},
    'div[1]': {width:'90%', position:'absolute', top:'40%', display: 'none'},
    'ul/li': {display: 'none'},

.. s6:: actions

    ['div[0]', 'fade in', '0.3'],
    ['div[1]', 'fade in', '2.0'],
    ['ul/li[0]', 'fade in', '0.3'],


Sphinx 1.2 の追加機能
======================

* Python3.3対応(要docutils0.10)
* sphinx.ext.linkcode拡張

  (function等からソースへリンク）

* reST読み取り後の内部データをXML出力
* Sphinx開発者向けガイドドキュメント
* 日本語Dir/File名を使用可能
* 翻訳機能の対象を拡大(または不具合修正)
* texinfo機能の大幅強化
* autodocのデバッグ効率向上


.. s6:: effect slide

.. s6:: styles

    'ul/li': {display: 'none', fontSize:'90%'},

.. s6:: actions

    ['ul/li[0]', 'fade in', '0.3'],
    ['ul/li[1]', 'fade in', '0.3'],
    ['ul/li[2]', 'fade in', '0.3'],
    ['ul/li[3]', 'fade in', '0.3'],
    ['ul/li[4]', 'fade in', '0.3'],
    ['ul/li[5]', 'fade in', '0.3'],
    ['ul/li[6]', 'fade in', '0.3'],
    ['ul/li[7]', 'fade in', '0.3'],


翻訳機能の対象拡大（不具合？）
==============================

* 画像(figure)のキャプション
* 脚注(footnote)のcite
* 用語定義(definition)の用語
* 用語集(glossary)の用語
* 索引(index)の用語
* 翻訳文章中のリンクが壊れる問題
* docfield, versionadd系

.. s6:: effect slide

.. s6:: styles

    'ul/li': {display: 'none', fontSize:'90%'},

.. s6:: actions

    ['ul/li[0]', 'fade in', '0.3'],
    ['ul/li[1]', 'fade in', '0.3'],
    ['ul/li[2]', 'fade in', '0.3'],
    ['ul/li[3]', 'fade in', '0.3'],
    ['ul/li[4]', 'fade in', '0.3'],
    ['ul/li[5]', 'fade in', '0.3'],
    ['ul/li[6]', 'fade in', '0.3'],



Sphinx 1.2 の修正機能
======================

* `make text` で日本語だと文字幅がガタガタになる問題
* intersphinxのマッピングが期待順にならない問題(py33)
* etc. etc...

.. s6:: effect slide

.. s6:: styles

    'ul/li': {display: 'none', fontSize:'90%'},

.. s6:: actions

    ['ul/li[0]', 'fade in', '0.3'],
    ['ul/li[1]', 'fade in', '0.3'],
    ['ul/li[2]', 'fade in', '0.3'],

Sphinx 1.2 言語カタログ追加
============================

* Norwegian bokmaal
* Slovak
* Hungarian
* Basque
* Hebrew
* 現在: **32言語**

.. s6:: effect slide


公式ドキュメント多言語化計画
=============================

* 日本語公式ドキュメントは今まで直接書き換えていました:

  .. code-block:: rst

      .. Available builders
      .. ==================

      利用可能なビルダー
      ==================


* 今後は翻訳作業を Transifex_ でやります
* Sphinx i18n機能の **モデルケース**
* 翻訳のお手伝い募集中です！

.. _Transifex: https://www.transifex.com/projects/p/sphinx-doc-1_2_0/

.. s6:: effect slide

.. s6:: styles

    'ul/li': {display: 'none', fontSize:'90%'},

.. s6:: actions

    ['ul/li[0]', 'fade in', '0.3'],
    ['ul/li[1]', 'fade in', '0.3'],
    ['ul/li[2]', 'fade in', '0.3'],
    ['ul/li[3]', 'fade in', '0.3'],


おまけ： Sphinx本アンケート
=============================

* どんな本なら読みたいか、アンケート！
* http://goo.gl/MU7zO

