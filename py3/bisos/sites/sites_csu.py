# -*- coding: utf-8 -*-

""" #+begin_org
* ~[Summary]~ :: =CS-Lib= A RO service for registration of Boxes at a site.
#+end_org """

####+BEGIN: b:py3:cs:file/dblockControls :classification "cs-u"
""" #+begin_org
* [[elisp:(org-cycle)][| /Control Parameters Of This File/ |]] :: dblk ctrls classifications=cs-u
#+BEGIN_SRC emacs-lisp
(setq-local b:dblockControls t) ; (setq-local b:dblockControls nil)
(put 'b:dblockControls 'py3:cs:Classification "cs-u") ; one of cs-mu, cs-u, cs-lib, bpf-lib, pyLibPure
#+END_SRC
#+RESULTS:
: cs-u
#+end_org """
####+END:

####+BEGIN: b:prog:file/proclamations :outLevel 1
""" #+begin_org
* *[[elisp:(org-cycle)][| Proclamations |]]* :: Libre-Halaal Software --- Part Of BISOS ---  Poly-COMEEGA Format.
** This is Libre-Halaal Software. © Neda Communications, Inc. Subject to AGPL.
** It is part of BISOS (ByStar Internet Services OS)
** Best read and edited  with Blee in Poly-COMEEGA (Polymode Colaborative Org-Mode Enhance Emacs Generalized Authorship)
#+end_org """
####+END:

####+BEGIN: b:prog:file/particulars :authors ("./inserts/authors-mb.org")
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars |]]* :: Authors, version
** This File: /bisos/git/bxRepos/bisos-pip/siteRegistrars/py3/bisos/siteRegistrars/csSiteRegBox.py
** Authors: Mohsen BANAN, http://mohsen.banan.1.byname.net/contact
#+end_org """
####+END:

####+BEGINNOT: b:py3:file/particulars-csInfo :status "inUse"
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars-csInfo |]]*
#+end_org """
import typing
csInfo: typing.Dict[str, typing.Any] = { 'moduleName': ['csSiteRegBox'], }
csInfo['version'] = '202401192758'
csInfo['status']  = 'inUse'
csInfo['panel'] = "[[../../panels/_nodeBase_/fullUsagePanel-en.org]]"
csInfo['groupingType'] = 'IcmGroupingType-pkged'
csInfo['cmndParts'] = 'IcmCmndParts[common] IcmCmndParts[param]'
####+END:

""" #+begin_org
* [[elisp:(org-cycle)][| ~Description~ |]] :: [[file:/bisos/git/auth/bxRepos/blee-binders/bisos-core/PyFwrk/bisos-pip/bisos.cs/_nodeBase_/fullUsagePanel-en.org][BISOS CmndSvcs Panel]]   [[elisp:(org-cycle)][| ]]
** TODO Document this module.
** TODO Add sectioning for Invoker and performer.
** Relevant Panels:
** Status: In use with BISOS
** /[[elisp:(org-cycle)][| Planned Improvements |]]/ :
*** TODO complete fileName in particulars.
#+end_org """

####+BEGIN: b:prog:file/orgTopControls :outLevel 1
""" #+begin_org
* [[elisp:(org-cycle)][| Controls |]] :: [[elisp:(delete-other-windows)][(1)]] | [[elisp:(show-all)][Show-All]]  [[elisp:(org-shifttab)][Overview]]  [[elisp:(progn (org-shifttab) (org-content))][Content]] | [[file:Panel.org][Panel]] | [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] | [[elisp:(bx:org:run-me)][Run]] | [[elisp:(bx:org:run-me-eml)][RunEml]] | [[elisp:(progn (save-buffer) (kill-buffer))][S&Q]]  [[elisp:(save-buffer)][Save]]  [[elisp:(kill-buffer)][Quit]] [[elisp:(org-cycle)][| ]]
** /Version Control/ ::  [[elisp:(call-interactively (quote cvs-update))][cvs-update]]  [[elisp:(vc-update)][vc-update]] | [[elisp:(bx:org:agenda:this-file-otherWin)][Agenda-List]]  [[elisp:(bx:org:todo:this-file-otherWin)][ToDo-List]]

#+end_org """
####+END:

####+BEGIN: b:py3:file/workbench :outLevel 1
""" #+begin_org
* [[elisp:(org-cycle)][| Workbench |]] :: [[elisp:(python-check (format "/bisos/venv/py3/bisos3/bin/python -m pyclbr %s" (bx:buf-fname))))][pyclbr]] || [[elisp:(python-check (format "/bisos/venv/py3/bisos3/bin/python -m pydoc ./%s" (bx:buf-fname))))][pydoc]] || [[elisp:(python-check (format "/bisos/pipx/bin/pyflakes %s" (bx:buf-fname)))][pyflakes]] | [[elisp:(python-check (format "/bisos/pipx/bin/pychecker %s" (bx:buf-fname))))][pychecker (executes)]] | [[elisp:(python-check (format "/bisos/pipx/bin/pycodestyle %s" (bx:buf-fname))))][pycodestyle]] | [[elisp:(python-check (format "/bisos/pipx/bin/flake8 %s" (bx:buf-fname))))][flake8]] | [[elisp:(python-check (format "/bisos/pipx/bin/pylint %s" (bx:buf-fname))))][pylint]]  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

####+BEGIN: b:py3:cs:orgItem/basic :type "=PyImports= " :title "*Py Library IMPORTS*" :comment "-- with classification based framework/imports"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  =PyImports=  [[elisp:(outline-show-subtree+toggle)][||]] *Py Library IMPORTS* -- with classification based framework/imports  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

####+BEGIN: b:py3:cs:framework/imports :basedOn "classification"
""" #+begin_org
** Imports Based On Classification=cs-u
#+end_org """
from bisos import b
from bisos.b import cs
from bisos.b import b_io
from bisos.common import csParam

import collections
####+END:

from pathlib import Path
from bisos.bpo import bpo
from bisos.platform import platformBpo
from bisos.basics import pathPlus

####+BEGIN: b:py3:cs:orgItem/section :title "Common Parameters Specification" :comment "based on cs.param.CmndParamDict -- As expected from CSU-s"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  /Section/    [[elisp:(outline-show-subtree+toggle)][||]] *Common Parameters Specification* based on cs.param.CmndParamDict -- As expected from CSU-s  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "examples_csu" :comment "" :parsMand "" :parsOpt "perfName" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<examples_csu>>  =verify= parsOpt=perfName ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class examples_csu(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'perfName', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             perfName: typing.Optional[str]=None,  # Cs Optional Param
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {'perfName': perfName, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
        perfName = csParam.mappedValue('perfName', perfName)
####+END:
        if self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Basic example command.
        #+end_org """): return(cmndOutcome)

        self.captureRunStr(""" #+begin_org
#+begin_src sh :results output :session shared
sitesManage.cs
#+end_src
#+RESULTS:
#+begin_example
,*    ##########
=======  /bisos/venv/py3/dev-bisos3/bin/sitesManage.cs   ===========
#######  /Command Service (CS) Brief Usage/  ##########
sitesManage.cs -i commonExamples    # Help, Model, icmOptionsExample
sitesManage.cs -i describe | emlVisit
sitesManage.cs -i examples | icmToEmlVisit
sitesManage.cs -i visit
emlVisit -v -n showRun -i gotoPanel /bisos/venv/py3/dev-bisos3/bin/sitesManage.cs
#######  *Blee Command Services Player (Update, Start, StartUpdated)*  ##########
sitesManage.cs -v 20  -i bleepUpdate
sitesManage.cs -v 20  -i bleepPlay
sitesManage.cs -v 20  -i bleepPlayUpdated
#######  =Sites and Selected Site=  ##########
sitesManage.cs  -i sitesInfo           # Sites Information
=======  =Related BASH Scripts=  ==========
siteManage.sh
#+end_example
        #+end_org """)
        if self.justCaptureP(): return cmndOutcome

        bro_rawBisosSite = "/bisos/git/bxRepos/bxObjects/bro_rawBisos/bro_rawBisosSite"

        od = collections.OrderedDict
        cmnd = cs.examples.cmndEnter
        literal = cs.examples.execInsert

        this_bpoId = platformBpo.platformBpoId()

        if this_bpoId is None:
            this_bpoId = bro_rawBisosSite

        cs.examples.menuChapter('=Sites and Selected Site=')

        cmnd('sitesInfo', comment=" # Sites Information")
        # cmnd('cmdbSummary', pars=perfNamePars, comment=" # remote obtain facter data, use it to summarize for cmdb")

        cs.examples.menuSection('=Site Base -- /bisos/var/sites/selected -- /bisos/site=')

        cmnd('siteBase', pars=od([('bpoId', this_bpoId),]), args="update")
        if this_bpoId != bro_rawBisosSite:
            cmnd('siteBase', pars=od([('bpoId', bro_rawBisosSite),]), args="update", comment=f"# Set at rawBisos Construction")

        cmnd('siteBase', args="obtain")
        cmnd('siteBase', args="obtain", comment=f"| xargs ls -l  # Show the symlink")
        cmnd('siteBase', args="obtain", comment=f"| xargs realpath  # Show the symlink")

        cs.examples.menuSection('=Site Bisos Add/Select -- Converted From site_lib.sh=')

        cmnd('siteBisosAdd', args="pis_exampleSite", comment=f"# vis_siteBisosAdd -- create /bisos/var/sites/<siteBxoId>")
        cmnd('siteBisosSelect', args="pis_exampleSite", comment=f"# vis_siteBisosSelect -- update /bisos/var/sites/selected")

        cs.examples.menuSection('=Related BASH Scripts=')

        literal("siteManage.sh")

        return(cmndOutcome)


####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :sep nil :title "CmndSvc" :anchor ""  :extraInfo "Command Services Section"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*     [[elisp:(outline-show-subtree+toggle)][| _Invoker Only CmndSvc_: |]]  Command Services Section  [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END:


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "sitesInfo" :comment "" :extent "verify" :ro "noCli" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv "methodInvokeArg"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<sitesInfo>>  =verify= ro=noCli pyInv=methodInvokeArg   [[elisp:(org-cycle)][| ]]
#+end_org """
class sitesInfo(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}
    rtInvConstraints = cs.rtInvoker.RtInvoker.new_noRo() # NO RO From CLI

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             methodInvokeArg: typing.Any=None,   # pyInv Argument
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
####+END:
        if self.cmndDocStr(""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Map svcName to portNu. Outcome is a list of port numbers.
        #+end_org """): return(cmndOutcome)

        self.captureRunStr(""" #+begin_org
#+begin_src sh :results output :session shared
  sitesManage.cs -i sitesInfo
#+end_src
#+RESULTS:
: ** cmnd=
: ls -l /bisos/site
: ls -ld /bisos/var/sites/*
: ls -l /bisos/var/sites/selected
:
: lrwxrwxrwx 1 bystar bisos 25 Jan 31 11:12 /bisos/site -> /bisos/var/sites/selected
: lrwxrwxrwx 1 bystar bisos 29 Jun 22  2024 /bisos/var/sites/pis_superSiteNeda -> /bxo/r3/iso/pis_superSiteNeda
: lrwxrwxrwx 1 bystar bisos 29 Jun 22  2024 /bisos/var/sites/selected -> /bxo/r3/iso/pis_superSiteNeda
: lrwxrwxrwx 1 bystar bisos 29 Jun 22  2024 /bisos/var/sites/selected -> /bxo/r3/iso/pis_superSiteNeda
        #+end_org """)
        if self.justCaptureP(): return cmndOutcome

        if b.subProc.Op(outcome=cmndOutcome, log=1).bash(
                f"""
ls -l /bisos/site
ls -ld /bisos/var/sites/*
ls -l /bisos/var/sites/selected
""",
        ).isProblematic():  return(b_io.eh.badOutcome(cmndOutcome))

        result="Review the Above File Listings"
        return cmndOutcome.set(opResults=result,)


####+BEGIN: b:py3:cs:orgItem/section :title "Site Bisos Base -- Converted From /bisos/core/bsip/bin/site_lib.sh" :comment "vis_siteBisosBase, vis_siteBisosAdd, vis_siteBisosSelect"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  /Section/    [[elisp:(outline-show-subtree+toggle)][||]] *Site Bisos Base* -- Converted From /bisos/core/bsip/bin/site_lib.sh -- vis_siteBisosBase, vis_siteBisosAdd, vis_siteBisosSelect  [[elisp:(org-cycle)][| ]]

NOTE :: The =siteBase= Cmnd below is a *copy* (not a move) of =bisos.platform='s
=platformBases_csu.siteBase=, brought here so that =bisos.sites= becomes the
single, complete owner of site-symlink management. Unlike the platform copy
(marked "NOTYET, Incomplete -- Selected itself needs to be updated based on
bpoId"), this version's =update= action delegates to =siteBisosSelect=, which
does perform the bpoId-specific re-pointing -- resolving that gap here.
=bisos.platform='s own copy is intentionally left as-is (out of scope for
this repo).
#+end_org """
####+END:


####+BEGIN: b:py3:cs:func/typing :funcName "siteBisosBase" :funcType "extTyped" :deco "track"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /siteBisosBase/  deco=track  [[elisp:(org-cycle)][| ]]
#+end_org """
@cs.track(fnLoc=True, fnEntry=True, fnExit=True)
def siteBisosBase(
####+END:
) -> Path:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ]  Converted from site_lib.sh's vis_siteBisosBase. Base dir under which
per-site and =selected= symlinks live.
    #+end_org """

    return Path("/bisos/var/sites")


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "siteBase" :comment "" :extent "verify" :ro "cli" :parsMand "" :parsOpt "bpoId" :argsMin 1 :argsMax 1 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<siteBase>>  =verify= parsOpt=bpoId argsMin=1 argsMax=1 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class siteBase(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'bpoId', ]
    cmndArgsLen = {'Min': 1, 'Max': 1,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             bpoId: typing.Optional[str]=None,  # Cs Optional Param
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {'bpoId': bpoId, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
        bpoId = csParam.mappedValue('bpoId', bpoId)
####+END:
        if self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  With bpoId update or obtain /bisos/var/sites/selected and /bisos/site.
*** Copied from bisos.platform.platformBases_csu.siteBase; update delegates to
    siteBisosSelect so bpoId-specific re-pointing actually happens here, and
    additionally ensures /bisos/site itself is symlinked to
    /bisos/var/sites/selected (siteBisosSelect only updates =selected=,
    matching vis_siteBisosSelect's original semantics -- the /bisos/site
    re-link is siteBase's own responsibility, mirroring how
    bisos.platform's siteBase re-links /bisos/platform).
        #+end_org """): return(cmndOutcome)

        action = self.cmndArgsGet("0&1", cmndArgsSpecDict, argsList)[0]

        if action == "update":
            if not bpoId:
                return failed(cmndOutcome)
            selectOutcome = siteBisosSelect().pyCmnd(argsList=[bpoId])
            if selectOutcome.isProblematic():
                return b_io.eh.badOutcome(cmndOutcome)

            pathPlus.symlink_update(siteBisosBase().joinpath("selected"), Path("/bisos/site"))

            return cmndOutcome.set(opResults=Path("/bisos/site"))

        elif action == "obtain":
            return cmndOutcome.set(opResults=Path("/bisos/site"))

        else:
            return failed(cmndOutcome)


####+BEGIN: b:py3:cs:method/args :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList "self"
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /cmndArgsSpec/ deco=default  deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self, ):
####+END:
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = cs.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0&1",
            argName="action",
            argDefault='',
            argChoices=['update', 'obtain'],
            argDescription="One argument, as action"
        )
        return cmndArgsSpecDict


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "siteBisosAdd" :comment "" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 1 :argsMax 1 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<siteBisosAdd>>  =verify= argsMin=1 argsMax=1 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class siteBisosAdd(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 1, 'Max': 1,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
####+END:
        if self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Converted from site_lib.sh's vis_siteBisosAdd. With siteBxoId,
create/update /bisos/var/sites/<siteBxoId> to point at that site's bpo base dir.
        #+end_org """): return(cmndOutcome)

        siteBxoId = self.cmndArgsGet("0", cmndArgsSpecDict, argsList)

        bpoBaseDir = bpo.bpoBaseDir_obtain(siteBxoId)
        bpoBasePath = Path(bpoBaseDir)

        sitesBase = siteBisosBase()
        sitesBase.mkdir(parents=True, exist_ok=True)

        pathPlus.symlink_update(bpoBasePath, sitesBase.joinpath(siteBxoId))

        return cmndOutcome.set(opResults=str(sitesBase.joinpath(siteBxoId)))


####+BEGIN: b:py3:cs:method/args :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList "self"
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /cmndArgsSpec/ deco=default  deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self, ):
####+END:
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = cs.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0",
            argName="siteBxoId",
            argDefault='',
            argChoices=[],
            argDescription="siteBxoId to be added under /bisos/var/sites/"
        )
        return cmndArgsSpecDict


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "siteBisosSelect" :comment "" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 1 :argsMax 1 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<siteBisosSelect>>  =verify= argsMin=1 argsMax=1 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class siteBisosSelect(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 1, 'Max': 1,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
####+END:
        if self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Converted from site_lib.sh's vis_siteBisosSelect. With siteBxoId,
update /bisos/var/sites/selected to point at that site's bpo base dir --
this is what /bisos/site ultimately resolves through.
        #+end_org """): return(cmndOutcome)

        siteBxoId = self.cmndArgsGet("0", cmndArgsSpecDict, argsList)

        bpoBaseDir = bpo.bpoBaseDir_obtain(siteBxoId)
        bpoBasePath = Path(bpoBaseDir)

        sitesBase = siteBisosBase()
        sitesBase.mkdir(parents=True, exist_ok=True)

        pathPlus.symlink_update(bpoBasePath, sitesBase.joinpath("selected"))

        return cmndOutcome.set(opResults=str(sitesBase.joinpath("selected")))


####+BEGIN: b:py3:cs:method/args :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList "self"
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /cmndArgsSpec/ deco=default  deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self, ):
####+END:
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = cs.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0",
            argName="siteBxoId",
            argDefault='',
            argChoices=[],
            argDescription="siteBxoId to become the /bisos/var/sites/selected target"
        )
        return cmndArgsSpecDict


####+BEGIN: b:py3:cs:framework/endOfFile :basedOn "classification"
""" #+begin_org
* [[elisp:(org-cycle)][| *End-Of-Editable-Text* |]] :: emacs and org variables and control parameters
#+end_org """

#+STARTUP: showall

### local variables:
### no-byte-compile: t
### end:
####+END:
