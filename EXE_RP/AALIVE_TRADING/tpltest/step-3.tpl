 
    <div class="step">
            <div class="moduleTitle hd">
                    <h2>{$APP.LBL_CR_INVESTOR_PROFILE} - {$APP.LBL_CR_LEGAL_ENTITIES}</h2>
                    <h3>{$APP.LBL_CR_INVESTMENT_GUIDELINES} - {$APP.LBL_CR_STEP} 3</h3>
                    <div class="clear"></div>
            </div>
            <div class="row portfolio-overview">
                    <div class="small-12 column">
                            <p><b>{$APP.LBL_INCOME_CERTAINTY}</b><br><br>
                            </p>
                            <form class="step_form">
                                    <p>
    <input type="radio" name="income_certainty" value="kurzfristig gesichert, hohe Schwankungen" {if $data->income_certainty eq "kurzfristig gesichert, hohe Schwankungen"}checked="checked"{/if}>{$APP.LBL_ANSWER_GIIresult_3_1_TEXT}<br>
    <input type="radio" name="income_certainty" value="mittelfristig gesichert, geringe Schwankungen, Unsicherheit in der Zukunft" {if $data->income_certainty eq "mittelfristig gesichert, geringe Schwankungen, Unsicherheit in der Zukunft"}checked="checked"{/if}>{$APP.LBL_ANSWER_GIIresult_3_2_TEXT}<br>
    <input type="radio" name="income_certainty" value="langfristig gesichert, Einnahmen aus verschiedenen Quellen" {if $data->income_certainty eq "langfristig gesichert, Einnahmen aus verschiedenen Quellen"}checked="checked"{/if}>{$APP.LBL_ANSWER_GIIresult_3_3_TEXT}<br>
    <input type="radio" name="income_certainty" value="nonfound" {if $data->income_certainty eq "nonfound"}checked="checked"{/if}>{$APP.LBL_ANSWER_GIIresult_3_4_TEXT}<br>
                                    </p>
                            </form>
                    </div>
            </div>
            <a href="javascript:void(0)" onclick="SUGAR.RiskWorkflow.next()" data-step="4" class="button gen-button next" >{$APP.LBL_CR_NEXT}</a>
    </div> 
