 
    <div class="step">
            <div class="moduleTitle hd">
                    <h2>{$APP.LBL_CR_INVESTOR_PROFILE} - {$APP.LBL_CR_LEGAL_ENTITIES}</h2>
                    <h3>{$APP.LBL_CR_INVESTMENT_GUIDELINES} - {$APP.LBL_CR_STEP} 12</h3>
                    <div class="clear"></div>
            </div>
            <div class="row portfolio-overview">
                    <div class="small-12 column">
                            <p><b>{$APP.LBL_ACCEPTABLE_YRS_LOSS}</b><br><br>
                            </p>
                            <form class="step_form">
                                    <p>
    <input type="radio" name="acceptable_yrs_loss" value="< 5%" {if $data->acceptable_yrs_loss eq "< 5%"}checked="checked"{/if}>{$APP.LBL_ANSWER_GIIresult_12_1_TEXT}<br>
    <input type="radio" name="acceptable_yrs_loss" value="6% - 10%" {if $data->acceptable_yrs_loss eq "6% - 10%"}checked="checked"{/if}>{$APP.LBL_ANSWER_GIIresult_12_2_TEXT}<br>
    <input type="radio" name="acceptable_yrs_loss" value="11% - 20%" {if $data->acceptable_yrs_loss eq "11% - 20%"}checked="checked"{/if}>{$APP.LBL_ANSWER_GIIresult_12_3_TEXT}<br>
    <input type="radio" name="acceptable_yrs_loss" value=">20%" {if $data->acceptable_yrs_loss eq ">20%"}checked="checked"{/if}>{$APP.LBL_ANSWER_GIIresult_12_4_TEXT}<br>
                                    </p>
                            </form>
                    </div>
            </div>
            <a href="javascript:void(0)" onclick="SUGAR.RiskWorkflow.next()" data-step="13" class="button gen-button next" >{$APP.LBL_CR_NEXT}</a>
    </div> 
