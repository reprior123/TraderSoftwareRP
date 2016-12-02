 
    <div class="step">
            <div class="moduleTitle hd">
                    <h2>{$APP.LBL_CR_INVESTOR_PROFILE} - {$APP.LBL_CR_LEGAL_ENTITIES}</h2>
                    <h3>{$APP.LBL_CR_INVESTMENT_GUIDELINES} - {$APP.LBL_CR_STEP} 10</h3>
                    <div class="clear"></div>
            </div>
            <div class="row portfolio-overview">
                    <div class="small-12 column">
                            <p><b>{$APP.LBL_EXPECTED_RETURN}</b><br><br>
                            </p>
                            <form class="step_form">
                                    <p>
    <input type="radio" name="expected_return" value="< 2%" {if $data->expected_return eq "< 2%"}checked="checked"{/if}>{$APP.LBL_ANSWER_GIIresult_10_1_TEXT}<br>
    <input type="radio" name="expected_return" value="2% - 4%" {if $data->expected_return eq "2% - 4%"}checked="checked"{/if}>{$APP.LBL_ANSWER_GIIresult_10_2_TEXT}<br>
    <input type="radio" name="expected_return" value="4% - 6%" {if $data->expected_return eq "4% - 6%"}checked="checked"{/if}>{$APP.LBL_ANSWER_GIIresult_10_3_TEXT}<br>
    <input type="radio" name="expected_return" value="6% - 8%" {if $data->expected_return eq "6% - 8%"}checked="checked"{/if}>{$APP.LBL_ANSWER_GIIresult_10_4_TEXT}<br>
                                    </p>
                            </form>
                    </div>
            </div>
            <a href="javascript:void(0)" onclick="SUGAR.RiskWorkflow.next()" data-step="11" class="button gen-button next" >{$APP.LBL_CR_NEXT}</a>
    </div> 
