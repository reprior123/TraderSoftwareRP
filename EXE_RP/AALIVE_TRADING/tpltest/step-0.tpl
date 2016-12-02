 
    <div class="step">
            <div class="moduleTitle hd">
                    <h2>{$APP.LBL_CR_INVESTOR_PROFILE} - {$APP.LBL_CR_LEGAL_ENTITIES}</h2>
                    <h3>{$APP.LBL_CR_INVESTMENT_GUIDELINES} - {$APP.LBL_CR_STEP} 0</h3>
                    <div class="clear"></div>
            </div>
            <div class="row portfolio-overview">
                    <div class="small-12 column">
                            <p><b>{$APP.LBL_NONFOUND}</b><br><br>
                            </p>
                            <form class="step_form">
                                    <p>
    <input type="radio" name="nonfound" value="nonfound" {if $data->nonfound eq "nonfound"}checked="checked"{/if}>{$APP.LBL_ANSWER_GIIresult_0_1_TEXT}<br>
    <input type="radio" name="nonfound" value="nonfound" {if $data->nonfound eq "nonfound"}checked="checked"{/if}>{$APP.LBL_ANSWER_GIIresult_0_2_TEXT}<br>
    <input type="radio" name="nonfound" value="nonfound" {if $data->nonfound eq "nonfound"}checked="checked"{/if}>{$APP.LBL_ANSWER_GIIresult_0_3_TEXT}<br>
    <input type="radio" name="nonfound" value="nonfound" {if $data->nonfound eq "nonfound"}checked="checked"{/if}>{$APP.LBL_ANSWER_GIIresult_0_4_TEXT}<br>
                                    </p>
                            </form>
                    </div>
            </div>
            <a href="javascript:void(0)" onclick="SUGAR.RiskWorkflow.next()" data-step="1" class="button gen-button next" >{$APP.LBL_CR_NEXT}</a>
    </div> 
